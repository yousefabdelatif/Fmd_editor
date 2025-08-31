from pathlib import Path
import shutil


class EditorModel:
    def __init__(self):
        self.__Template: str = None

    def loadTemplate(self, template_version: str) -> None:

        filePath = Path("./Templates") / (template_version.replace(".", "_") + ".html")
        try:
            with open(filePath, "r") as file:
                self.__Template = file.read()

        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file not found at {filePath.absolute()}")
        except IOError:
            raise IOError()

    @property
    def template(self):
        return self.__Template

    def export_as_html(self,src:str,path:Path):
        with open(path.absolute(), "w") as file:
                file.write(src)


