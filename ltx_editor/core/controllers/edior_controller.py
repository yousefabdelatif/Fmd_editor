from PySide6.QtWidgets import *

from ltx_editor import ProjectController
from pathlib import Path


class EditorController:
    __template: str
    __editor: QMainWindow
    __projectControllerInstance: ProjectController
    def __init__(self):
        self.__projectControllerInstance = ProjectController()
        self.loadTemplate()
       # self.__ui= editor_window.Ui_ltx_editor()
       # self.__editorWindow = QMainWindow()
       # self.__ui.setupUi(self.__editorWindow)
       # self.__editorWindow.show()
        self.__projectControllerInstance.loadProjact(Path("D:/ECE/New folder"))





    def loadTemplate(self):
        if Path.exists(Path("Template_001.html")):
            with open(Path("Template_001.html"),'r') as file:
                self.__template=file.read()





