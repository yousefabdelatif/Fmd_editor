from ltx_editor.controllers.projectController import ProjectController
from ltx_editor.ui.Ui_ltx_editor import *
from PySide6.QtWidgets import *
from pathlib import Path


class EditorController:

    def __init__(self):
        self.__projectControllerInstance = ProjectController()

        self.__ui= Ui_ltx_editor()
        self.__editorWindow = QMainWindow()


    def view(self):
        self.__ui.setupUi(self.__editorWindow)
        self.__ui.action_newproject.triggered.connect(self.__on_create_project)
        self.__ui.actionOpenProject.triggered.connect(self.__on_open_project)
        self.__ui.actionSave.triggered.connect(self.__on_save_date)
        self.__ui.TextEditor.textChanged.connect(self.__on_Code_changed)
        self.__editorWindow.show()

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
                self.__ui.TextEditor.setText(self.__projectControllerInstance.getProjectData())

                # Show a success message to the user
                QMessageBox.information(
                    self.__editorWindow,
                    "Project Opened",
                    f"Project loaded successfully from:\n{folder_path}"
                )
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
        self.__projectControllerInstance.save_project(self.__ui.TextEditor.toPlainText())








    def __on_Code_changed(self):
        print(self.__ui.TextEditor.toPlainText())











