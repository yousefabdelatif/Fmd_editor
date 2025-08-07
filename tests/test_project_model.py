import shutil

from pathlib import  Path

from ltx_editor.core.Constants import TEMPLATE_VERSION
from ltx_editor.models.project_model import ProjectModel


def test_create_project():
    path =Path("./")
    name ="testproject"
    model =ProjectModel()
    project_path = path / name
    dataPath =project_path /"src"/"data.itx"
    try:
        model.create_new(name=name, path=path, template_version=TEMPLATE_VERSION)

        assert (project_path/"config.json").exists()
        assert dataPath.exists()

        for file in ["src", "assets", "outputs"]:
            assert Path(project_path/file).exists()

        with open(dataPath, "r") as f:
            assert f.read() == "welcome to itx_editor"
    finally:

       shutil.rmtree(project_path, ignore_errors=True)
def test_load_project():
    path =Path("./tests")
    name ="testproject"
    model =ProjectModel()
    project_path = path / name
    dataPath =project_path /"src"/"data.itx"

    model.load_from_disk(path=project_path)

    assert model.projectName == "testproject"
    assert model.TemplateVersion == TEMPLATE_VERSION
    assert model.data == "welcome to itx_editor"
def test_save_data_to_disk():
    path =Path("./tests")
    name ="testproject"
    model =ProjectModel()
    project_path = path / "testproject"
    model.load_from_disk(project_path.absolute())

    dataPath =project_path /"src"/"data.itx"
    try:
        model.save_data_to_disk("data updated")
        with open(dataPath, "r") as f:
            assert f.read() == "data updated"
            assert model.data == "data updated"

    finally:
        with open(dataPath, "w") as f:
            f.write("welcome to itx_editor")













