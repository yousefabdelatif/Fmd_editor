from itx_compiler.itx_compiler import Itx_Compiler
from ltx_editor.controllers.edior_controller import  EditorController
import sys
from PySide6.QtWidgets import *





if __name__ == "__main__":
    app = QApplication(sys.argv)

    #e=EditorController()
    #e.view()
com =Itx_Compiler()
p=com.compile("<page><page><page><page></page><page><page></page></page><page>")
  #  sys.exit(app.exec())





