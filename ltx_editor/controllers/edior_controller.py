# Necessary imports that were missing
from ltx_editor.controllers.projectController import ProjectController
from ltx_editor.core.Constants import TEMPLATE_VERSION
from ltx_editor.models.editor_model import EditorModel
# from ltx_editor.ui.Ui_ltx_editor import * # Assuming these are not needed
# from ltx_editor.ui.Ui_ltx_editor_e import *

from pathlib import Path
import os
import subprocess
from PyQt6.QtWidgets import QInputDialog, QFileDialog, QMessageBox
from PyQt6.QtWebEngineWidgets import *
from PyQt6.QtCore import QTimer

from ltx_editor.ui.windows.Editor import EditorWindow
from ltx_editor.ui.widgets.TextEditor import Editor
from ltx_editor.ui.windows.start_dialog_window import StartDialogWindow


class EditorController:

    def __init__(self):
        self.__projectControllerInstance = ProjectController()
        self.__editor_model = EditorModel()
        self.__editorView = EditorWindow()
        self.__startDialogView = StartDialogWindow()
        # Initialize the timer, which was a cause of a crash
        self.__timer = QTimer()
        self.__timer.setSingleShot(True)
        self.__editor_model.loadTemplate("0.0.1")

    def view(self):
        self.__editorView.action_newproject.triggered.connect(self.__on_create_project)
        self.__editorView.actionOpenProject.triggered.connect(self.__on_open_project)
        self.__editorView.actionSave.triggered.connect(self.__on_save_date)

        # Connect to the TextEditor widget, which is a part of the EditorWindow
        self.__editorView.editor.textChanged.connect(self.__on_Code_changed)

        # Connect the timer to the save method
        self.__timer.timeout.connect(self.__on_save_date)

        self.__editorView.show()

    def __on_create_project(self):
        name, ok = QInputDialog.getText(
            self.__editorView,
            "Create new project",
            "Please enter your project name:"
        )

        if not (ok and name):
            return

        folder_path = QFileDialog.getExistingDirectory(
            self.__editorView,
            "Choose a project folder"
        )

        if folder_path:
            self.__projectControllerInstance.createNewProject(Path(folder_path), name=name)
            QMessageBox.information(
                self.__editorView,
                "Success",
                f"Project '{name}' was created successfully at:\n{folder_path}"
            )
            self.__editorView.show()
            self.__editorView.setWindowTitle(self.__projectControllerInstance.project_name)
        else:
            QMessageBox.warning(
                self.__editorView,
                "Action Cancelled",
                "Project creation was cancelled: No folder was selected."
            )

    def __on_open_project(self):
        try:
            folder_path_str = QFileDialog.getExistingDirectory(
                self.__editorView,
                "open a project folder"
            )

            if folder_path_str:
                folder_path = Path(folder_path_str)
                config_file_path = folder_path / "config.json"

                if config_file_path.exists():
                    self.__projectControllerInstance.loadProjact(folder_path)
                    self.__editorView.editor.setText(self.__projectControllerInstance.getProjectData())

                    QMessageBox.information(
                        self.__editorView,
                        "Project Opened",
                        f"Project loaded successfully from:\n{folder_path}"
                    )
                    self.__editorView.show()
                    self.__editorView.setWindowTitle(self.__projectControllerInstance.project_name)

                else:
                    QMessageBox.warning(
                        self.__editorView,
                        "Project Not Found",
                        f"No 'config.json' file found in the selected folder:\n{folder_path}"
                    )

            else:
                QMessageBox.warning(
                    self.__editorView,
                    "Action Cancelled",
                    "Project opening was cancelled: No folder was selected."
                )
        except Exception as e:
            print(e)

    def __on_save_date(self):
        # Correctly get the text from the editor widget
        self.__projectControllerInstance.save_project(self.__editorView.editor.text())

    def __on_Code_changed(self):
        self.__timer.stop()
        self.__timer.start(1000)
        # Correctly reference the Viewer widget and replace the text
        self.__editorView.Viewer.setHtml(
            self.__editor_model.template.replace("%%%%", self.__editorView.editor.text()))
        pass

    def __on_compile(self):
        print("fff")
        source_file = (self.__projectControllerInstance.base_path / 'src/data.tex').absolute()
        output_dir = (self.__projectControllerInstance.base_path / 'outputs').absolute()

        os.makedirs(output_dir, exist_ok=True)

        command = [
            r'C:\Users\pc\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdflatex.exe',
            '--output-directory',
            str(output_dir),
            str(source_file)
        ]

        try:
            # Use subprocess.run with check=True to raise an exception on error
            result = subprocess.run(command, check=True)
            print(f"Compilation successful! PDF is in the '{output_dir}' directory.")

            # The original code had a bug here, trying to print `args` which is not the error.
            # I've fixed it to show a success message.
            QMessageBox.information(
                self.__editorView,
                "Success",
                "Compilation successful!"
            )

            # Assuming self.__pdf_document and self.__editorView.Viewer exist and are the correct types
            from PyQt6.QtPdf import QPdfDocument
            self.__pdf_document = QPdfDocument()
            self.__editorView.Viewer.setDocument(self.__pdf_document)
            self.__pdf_document.load(str(output_dir / "data.pdf"))

        except FileNotFoundError:
            # Catch this specific error if the pdflatex executable isn't found
            QMessageBox.critical(self.__editorView, "Compilation Error",
                                 "pdflatex command not found. Make sure MiKTeX is installed and in your system PATH.")
        except subprocess.CalledProcessError as e:
            # This is the correct way to get the error output if compilation fails
            QMessageBox.critical(self.__editorView, "Compilation Failed",
                                 f"Compilation failed with exit code {e.returncode}. Check the log file for details.")
        except Exception:
            # The original code had a dangerous `os.system("exit")` here.
            # This is not a safe way to handle exceptions. I've replaced it
            # with a simple `pass` so the application doesn't close.
            pass
