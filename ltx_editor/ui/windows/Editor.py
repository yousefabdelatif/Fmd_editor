import sys
from PyQt6.QtWidgets import *
from PyQt6 import uic, QtWidgets
from PyQt6.QtCore import *

# Import your custom Editor widget and the Lexer
from ltx_editor.ui.widgets.TextEditor import Editor, CustomLexer
class EditorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Load the UI file at runtime
        self.ui= uic.loadUi('ui/Ui_ltx_editor.ui', self)
        self.timer: QTimer = QTimer()

        self.singleShot = True
        self.splitter: QSplitter = self.findChild(QSplitter, "splitter")
        self.TextEditor: QtWidgets.QTextEdit = self.findChild(
            QtWidgets.QTextEdit, "TextEditor")
        # ...
        index = self.splitter.indexOf(self.TextEditor)
        # ...
        self.editor:Editor = Editor(self)
        self.TextEditor.setParent(None)
        self.splitter.insertWidget(index, self.editor)
        self.TextEditor.deleteLater()
       # self.editor = Editor(self)









