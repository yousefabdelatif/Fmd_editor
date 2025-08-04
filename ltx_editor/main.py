import sys
from PySide6.QtWidgets import *
from ltx_editor.ui.main_window import MainWindow



if __name__ == "__main__":
    app = QApplication(sys.argv)

    appWindow = MainWindow()

    appWindow.show()

    sys.exit(app.exec())