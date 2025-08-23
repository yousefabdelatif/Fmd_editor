# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_ltx_editor_e.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt6.QtWidgets import (QApplication, QDialog, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_entry(object):
    def setupUi(self, entry):
        if not entry.objectName():
            entry.setObjectName(u"entry")
        entry.resize(500, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(entry.sizePolicy().hasHeightForWidth())
        entry.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(entry)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit_2 = QTextEdit(entry)
        self.textEdit_2.setObjectName(u"textEdit_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy1)
        self.textEdit_2.setUndoRedoEnabled(False)
        self.textEdit_2.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEdit_2)

        self.open_project_btn = QPushButton(entry)
        self.open_project_btn.setObjectName(u"open_project_btn")

        self.verticalLayout.addWidget(self.open_project_btn)

        self.create_project_btn = QPushButton(entry)
        self.create_project_btn.setObjectName(u"create_project_btn")

        self.verticalLayout.addWidget(self.create_project_btn)

        self.itx_editor = QLabel(entry)
        self.itx_editor.setObjectName(u"itx_editor")

        self.verticalLayout.addWidget(self.itx_editor)

        self.listWidget_2 = QListWidget(entry)
        self.listWidget_2.setObjectName(u"listWidget_2")

        self.verticalLayout.addWidget(self.listWidget_2)


        self.retranslateUi(entry)

        QMetaObject.connectSlotsByName(entry)
    # setupUi

    def retranslateUi(self, entry):
        entry.setWindowTitle(QCoreApplication.translate("entry", u"itx_editor", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("entry", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:xx-large; font-weight:700;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-in"
                        "dent:0px;\"><span style=\" font-size:xx-large; font-weight:700;\">Welcome to itx editor</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.open_project_btn.setText(QCoreApplication.translate("entry", u"open project", None))
        self.create_project_btn.setText(QCoreApplication.translate("entry", u"create new project", None))
        self.itx_editor.setText(QCoreApplication.translate("entry", u"recent project", None))
    # retranslateUi

