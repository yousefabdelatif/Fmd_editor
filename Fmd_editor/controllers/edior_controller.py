# Necessary imports that were missing

import os
import subprocess
from pathlib import Path

from PyQt6.QtCore import QTimer
from PyQt6.QtGui import *
from PyQt6.QtWidgets import QInputDialog, QFileDialog, QMessageBox

from Fmd_editor.controllers.projectController import ProjectController
from Fmd_editor.core.fmd_compiler.fmd_compiler import FmdCompiler
from Fmd_editor.models.editor_model import EditorModel
from Fmd_editor.ui.editor.Editor import EditorWindow


class EditorController:

    def __init__(self):
        self.__projectControllerInstance = ProjectController()
        self.__editor_model = EditorModel()
        self.__editorView = EditorWindow()
        # Initialize the timer, which was a cause of a crash
        self.__timer = QTimer()
        self.__timer.setSingleShot(True)
        self.compiler = FmdCompiler()

    def view(self):

        #actions handling
        self.__editorView.action_newproject.triggered.connect(self.__handel_create_project)
        self.__editorView.actionOpenProject.triggered.connect(self.__handle_open_project)
        self.__editorView.action_export_as_html.triggered.connect(self.__handel_export_as_html)
        # Connect to the TextEditor widget, which is a part of the EditorWindow
        self.__editorView.editor.textChanged.connect(self.__handel_code_change)

        # Connect the timer to the save method
        self.__timer.timeout.connect(self.__save_changes)

        # disable some props
        self.__editorView.editor.setEnabled(False)
        self.__editorView.reload_template_action.setEnabled(False)
        self.__editorView.action_export_as_html.setEnabled(False)

        self.__editorView.show()

    def __handel_create_project(self):
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
            self.__editorView.TextEditor.setEnabled(True)
        else:
            QMessageBox.warning(
                self.__editorView,
                "Action Cancelled",
                "Project creation was cancelled: No folder was selected."
            )

    def __handle_open_project(self):

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

                self.__editorView.editor.setEnabled(True)
                self.__editorView.reload_template_action.setEnabled(True)
                self.__editorView.action_export_as_html.setEnabled(True)
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



    def __handel_code_change(self):
        self.__timer.stop()
        self.__timer.start(1000)
        try:
            editor_text = self.__editorView.editor.text()
            html_code=self.compiler.compile(editor_text)
            self.__editorView.Viewer.setHtml(html_code)
        except Exception as e:
            QMessageBox.warning(
                self.__editorView,
                "Fatal error",
                f"could not rerender your document \n({e})"
            )



    def __handel_export_as_html(self):
        self.__projectControllerInstance.save_project(self.__editorView.editor.text())
        file_path = self.__projectControllerInstance.base_path / "outputs"

        try:
            editor_text = self.__editorView.editor.text()
            html_code = self.compiler.compile(editor_text)
            if file_path.exists():
                self.__editor_model.export_as_html(html_code,file_path/(
                    self.__projectControllerInstance.project_name + ".html"))
                QMessageBox.information(
                    self.__editorView,
                    "Success",
                    f"document export Successfully at{file_path/(
                    self.__projectControllerInstance.project_name + ".html")}"
                )
            else:
                shutil.rmtree(path, ignore_errors=True)
                print(path.absolute())
                raise RuntimeError("Export failed")

        except RuntimeError as e:

            QMessageBox.warning(
                self.__editorView,
                "Runtime error",
                f"document export failed"
            )


    def __save_changes(self):
        self.__projectControllerInstance.save_project(self.__editorView.editor.text())



