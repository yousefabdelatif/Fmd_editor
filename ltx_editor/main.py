from ltx_editor.controllers.edior_controller import  EditorController
import sys
from PySide6.QtWidgets import *





if __name__ == "__main__":
    app = QApplication(sys.argv)

    e=EditorController()
    e.view()

    sys.exit(app.exec())





