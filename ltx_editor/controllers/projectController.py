from pathlib import Path

from ltx_editor.core.Constants import TEMPLATE_VERSION
from ltx_editor.models.project_model import ProjectModel


class ProjectController:
    __currentProject :ProjectModel

    def __init__(self):
        self.__currentProject =ProjectModel()



    def createNewProject(self,path :Path,name:str):

        self.__currentProject.create_new(path=path,name=name,template_version=TEMPLATE_VERSION)


    def loadProjact(self, path: Path):
        self.__currentProject.load_from_disk(path=path)

    def save_project(self,data:str):
        self.__currentProject.save_data_to_disk(data)
    def deleteProject(self):
        pass

    def addNewPage(self):
        pass
    def deletePage(self):
        pass
    def editPageProperties(self):
        pass

    def getProjectData(self):
        return self.__currentProject.data



