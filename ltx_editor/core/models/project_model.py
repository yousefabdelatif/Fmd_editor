import json
from pathlib import Path
import shutil


class ProjectModel:


    def __init__(self):
        self.__projectName: str = None
        self.__basePath: Path = None
        self.__template_version: str = None
        self.__data: str = None
        self.__config_data: Path = None

    def save_data_to_disk(self, data: str):
        """Saves the project __data to the disk."""
        if not self.__basePath:
            raise ValueError("Cannot save __data: project base path is not set.")

        try:
            with open(self.__basePath / Path("src/data.itx"), "w") as file:
                self.__data = data
                file.write(data)
        except IOError as e:
            raise IOError(f"Failed to save data to disk: {e}")

    def load_from_disk(self, path: Path):
        """Loads a project from the specified path."""
        self.__basePath = path
        try:
            with open(path/ "config.json", "r") as file:
                self.__config_data = json.load(file)
                self.__projectName = self.__config_data.get('name')
                self.__template_version = self.__config_data.get('template_version')
                self.__basePath = Path(self.__config_data.get('basePath'))
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file not found at {self.__basePath / 'config.json'}")

        except json.JSONDecodeError:
            raise ValueError(f"Failed to parse config.json at {self.__basePath / 'config.json'}")


#import data.itx
        try:
            with open(self.__basePath / "src"/ "data.itx", "r") as file:
                self.__data = file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"Source file not found at {self.__basePath / 'src/data.itx'}")

    def create_new(self, name: str, path: Path, template_version: str):
        """Creates a new project directory structure and files."""
        project_path = path / name
        sub_directories = ["src", "assets", "outputs"]  # Typo fixed from 'assists'

        try:
            project_path.mkdir()
            for dir_name in sub_directories:
                (project_path / dir_name).mkdir()

            config_data = {
                "name": name,
                "template_version": template_version,
                "basePath": str(project_path.absolute())
            }

            with open(project_path / "config.json", "w") as config_file:
                json.dump(config_data, config_file, indent=4)

            initial_data = "welcome to itx_editor"
            with open(project_path / "src/data.itx", "w") as data_file:
                data_file.write(initial_data)

            self.__basePath = project_path
            self.__projectName = name
            self.__template_version = template_version
            self.__data = initial_data

        except IOError as e:
            shutil.rmtree(project_path, ignore_errors=True)
            raise IOError(f"An error occurred while creating the project: {e}")

    @property
    def data(self):
        return self.__data

    @property
    def projectName(self):
        return self.__projectName

    @property
    def TemplateVersion(self):
        return self.__template_version

