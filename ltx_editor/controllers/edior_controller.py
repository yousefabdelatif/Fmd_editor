import subprocess
import os

from ltx_editor.controllers.projectController import ProjectController
from ltx_editor.core.Constants import TEMPLATE_VERSION
from ltx_editor.models.editor_model import EditorModel
from ltx_editor.ui.Ui_ltx_editor import *
from ltx_editor.ui.Ui_ltx_editor_e import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from pathlib import Path


class EditorController:

    def __init__(self):
        self.__projectControllerInstance = ProjectController()
        self.__editor_model=EditorModel()

        self.__editorUI= Ui_ltx_editor()
        self.__entryDialogUI= Ui_entry()
        self.__editorWindow = QMainWindow()
        self.__entryDialog = QDialog()
        self.__editor_model.loadTemplate("0.0.1")
        self.__timer :QTimer=QTimer()



    def view(self):
        self.__editorUI.setupUi(self.__editorWindow)
        self.__entryDialogUI.setupUi(self.__entryDialog)
        self.__entryDialog.show()
        self.__entryDialogUI.create_project_btn.pressed.connect(self.__on_create_project)
        self.__entryDialogUI.open_project_btn.pressed.connect(self.__on_open_project)





        self.__editorUI.action_newproject.triggered.connect(self.__on_create_project)
        self.__editorUI.actionOpenProject.triggered.connect(self.__on_open_project)
        self.__editorUI.actionSave.triggered.connect(self.__on_save_date)
        self.__editorUI.TextEditor.textChanged.connect(self.__on_Code_changed)
        self.__timer.singleShot=True
        self.__timer.timeout.connect(self.__on_save_date)



    def __on_create_project(self):
        # 1. Get the project name from the user
        name, ok = QInputDialog.getText(
            self.__editorWindow,
            "Create new project",
            "Please enter your project name:"
        )

        # Check if the user clicked 'OK' AND provided a name.
        # If not, the function simply ends.
        if not (ok and name):
            # Optionally, you can show a message here for a canceled operation
            # QMessageBox.warning(self.__editorWindow, "Action Cancelled", "No project name was entered.")
            return

        # 2. Get the folder path from the user
        folder_path = QFileDialog.getExistingDirectory(
            self.__editorWindow,
            "Choose a project folder"
        )

        # Check if the user chose a folder (the path string is not empty).
        if folder_path:
            # Create the new project
            self.__projectControllerInstance.createNewProject(Path(folder_path), name=name)

            # Show a success message to the user
            QMessageBox.information(
                self.__editorWindow,
                "Success",
                f"Project '{name}' was created successfully at:\n{folder_path}"
            )
            self.__editorWindow.show()
            self.__entryDialog.hide()
            self.__editorWindow.setWindowTitle(self.__projectControllerInstance.project_name)
        else:
            # Show a message if the user cancelled the folder selection
            QMessageBox.warning(
                self.__editorWindow,
                "Action Cancelled",
                "Project creation was cancelled: No folder was selected."
            )
    def __on_open_project(self):
        folder_path_str = QFileDialog.getExistingDirectory(
            self.__editorWindow,
            "open a project folder"
        )

        # Check if the user chose a folder (the path string is not empty).
        if folder_path_str:
            # Correctly create a Path object for the selected folder
            folder_path = Path(folder_path_str)

            # Correctly check for config.json INSIDE the chosen folder
            config_file_path = folder_path / "config.json"

            if config_file_path.exists():
                # Load the project
                self.__projectControllerInstance.loadProjact(folder_path)
                self.__editorUI.TextEditor.setText(self.__projectControllerInstance.getProjectData())

                # Show a success message to the user
                QMessageBox.information(
                    self.__editorWindow,
                    "Project Opened",
                    f"Project loaded successfully from:\n{folder_path}"
                )
                self.__editorWindow.show()
                self.__entryDialog.hide()
                self.__editorWindow.setWindowTitle(self.__projectControllerInstance.project_name)

            else:
                # Show a warning if config.json is not found in the selected folder
                QMessageBox.warning(
                    self.__editorWindow,
                    "Project Not Found",
                    f"No 'config.json' file found in the selected folder:\n{folder_path}"
                )

        else:
            # Show a message if the user cancelled the folder selection
            QMessageBox.warning(
                self.__editorWindow,
                "Action Cancelled",
                "Project opening was cancelled: No folder was selected."
            )

    def __on_save_date(self):
        self.__projectControllerInstance.save_project(self.__editorUI.TextEditor.toPlainText())








    def __on_Code_changed(self):
        self.__timer.stop()
        self.__timer.start(1000)
        self.__editorUI.Viewer.setHtml(self.__editor_model.template.replace("%%%%", self.__editorUI.TextEditor.toPlainText()))
        pass



    def __on_compile(self):
        print("fff")
        source_file = (self.__projectControllerInstance.base_path / 'src/data.tex').absolute()
        output_dir = (self.__projectControllerInstance.base_path /'outputs').absolute()

        # Create the output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        # Build the command with the output directory flag
        command = [
            r'C:\Users\pc\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdflatex.exe',
            '--output-directory',
            str(output_dir),
            str(source_file)
        ]

        try:
            print(f"Compiling {source_file}...")
            error = subprocess.run(command, check=True).args
            print(f"Compilation successful! PDF is in the '{output_dir}' directory.")
            MessageBox.warning(
                self.__editorWindow,
                "Action Cancelled",
                error
            )





            # 3. Connect the QPdfView to the QPdfDocument

            self.__editorUI.Viewer.setDocument(self.__pdf_document)
            self.__pdf_document.load(str(output_dir/"data.pdf"))



        except FileNotFoundError:
            print("Error: The 'pdflatex' command was not found. "
                  "Make sure MiKTeX is installed and its bin directory is in your system PATH.")

        except subprocess.CalledProcessError:
            print("Compilation failed. Check the log file in the output directory for details.")
        except Exception:
            os.system("exit")















