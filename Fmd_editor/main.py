import sys

from PyQt6.QtWidgets import *

from Fmd_editor.controllers.edior_controller import EditorController

if __name__ == "__main__":
    app = QApplication(sys.argv)

    e = EditorController()
    e.view()

    sys.exit(app.exec())
