
# the Text editor widget is replaced by a QsciLexerCustom widget
#
#
#

from PyQt6 import uic, QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

# Import your custom CodeEditor widget and the Lexer
from fmd_editor.ui.editor.widgets.TextEditor import CodeEditor
from PyQt6.QtWebEngineWidgets import QWebEngineView



class EditorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('ui/editor/Editor.ui', self)
        self.timer: QTimer = QTimer()

        self.singleShot = True
        self.splitter: QSplitter = self.findChild(QSplitter, "splitter")
        self.TextEditor: QtWidgets.QTextEdit = self.findChild(
            QtWidgets.QTextEdit, "TextEditor")
        index = self.splitter.indexOf(self.TextEditor)
        # ...
        self.editor: CodeEditor = CodeEditor(self)
        self.TextEditor.setParent(None)
        self.splitter.insertWidget(index, self.editor)
        self.TextEditor.deleteLater()
        self.splitter.setSizes([800, 500])

