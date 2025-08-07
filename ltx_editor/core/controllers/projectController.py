from pathlib import Path

from ltx_editor import ProjectModel


class ProjectController:
    __currentProject :ProjectModel

    def __init__(self):
        self.__currentProject =ProjectModel()



    def createNewProject(self,path :Path,name:str):

        self.__currentProject.createNew(path=path,name=name)


    def loadProjact(self, path: Path):
        self.__currentProject.loadFromDisk(path=path)


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



