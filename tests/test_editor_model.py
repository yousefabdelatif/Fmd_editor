from ltx_editor.core.models.editor_model import EditorModel


def test_editor_model()->None:
    model = EditorModel()
    model.loadTemplate("0.0.1")
