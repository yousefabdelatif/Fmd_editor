from itx_compiler.itx_compiler import Itx_Compiler
from ltx_editor.controllers.edior_controller import EditorController
import sys
from PyQt6.QtWidgets import *
import re

if __name__ == "__main__":
    app = QApplication(sys.argv)

    e = EditorController()
    e.view()

    sys.exit(app.exec())
