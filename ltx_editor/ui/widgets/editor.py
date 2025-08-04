from PySide6.QtWidgets import *


class editor(QMainWindow):
 def __init__(self):
     super().__init__()
     self.setWindowTitle("Horizontal Layout Example")

     # Create the QHBoxLayout
     layout = QHBoxLayout()

     # Create the widgets
     text_editor = QPlainTextEdit()
     button = QPushButton("Click Me")

     # Add the widgets to the layout
     layout.addWidget(text_editor)
     layout.addWidget(button)

     # Set the layout for the main widget
     self.setLayout(layout)



