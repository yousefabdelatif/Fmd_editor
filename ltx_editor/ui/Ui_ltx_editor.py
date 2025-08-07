# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_ltx_editor.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_ltx_editor(object):
    def setupUi(self, ltx_editor):
        if not ltx_editor.objectName():
            ltx_editor.setObjectName(u"ltx_editor")
        ltx_editor.resize(804, 546)
        ltx_editor.setSizeIncrement(QSize(16, 9))
        self.action_newproject = QAction(ltx_editor)
        self.action_newproject.setObjectName(u"action_newproject")
        self.actionOpenProject = QAction(ltx_editor)
        self.actionOpenProject.setObjectName(u"actionOpenProject")
        self.actionfind = QAction(ltx_editor)
        self.actionfind.setObjectName(u"actionfind")
        self.actionFInd_replace = QAction(ltx_editor)
        self.actionFInd_replace.setObjectName(u"actionFInd_replace")
        self.actionExport = QAction(ltx_editor)
        self.actionExport.setObjectName(u"actionExport")
        self.actionimport = QAction(ltx_editor)
        self.actionimport.setObjectName(u"actionimport")
        self.actionSave = QAction(ltx_editor)
        self.actionSave.setObjectName(u"actionSave")
        self.centralwidget = QWidget(ltx_editor)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_6 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.TextEditor = QTextEdit(self.centralwidget)
        self.TextEditor.setObjectName(u"TextEditor")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TextEditor.sizePolicy().hasHeightForWidth())
        self.TextEditor.setSizePolicy(sizePolicy)
        self.TextEditor.setMinimumSize(QSize(500, 0))
        self.TextEditor.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_6.addWidget(self.TextEditor)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")

        self.horizontalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, -1, 0, -1)
        self.Recompile_btn = QPushButton(self.centralwidget)
        self.Recompile_btn.setObjectName(u"Recompile_btn")

        self.verticalLayout_6.addWidget(self.Recompile_btn)

        self.Viewer = QWebEngineView(self.centralwidget)
        self.Viewer.setObjectName(u"Viewer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(3)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Viewer.sizePolicy().hasHeightForWidth())
        self.Viewer.setSizePolicy(sizePolicy1)
        self.Viewer.setMinimumSize(QSize(270, 0))
        self.Viewer.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_6.addWidget(self.Viewer)


        self.horizontalLayout_6.addLayout(self.verticalLayout_6)

        ltx_editor.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ltx_editor)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 804, 22))
        self.menufile = QMenu(self.menubar)
        self.menufile.setObjectName(u"menufile")
        self.menuedit = QMenu(self.menubar)
        self.menuedit.setObjectName(u"menuedit")
        self.menuhelp = QMenu(self.menubar)
        self.menuhelp.setObjectName(u"menuhelp")
        ltx_editor.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ltx_editor)
        self.statusbar.setObjectName(u"statusbar")
        ltx_editor.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuedit.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())
        self.menufile.addAction(self.action_newproject)
        self.menufile.addAction(self.actionOpenProject)
        self.menufile.addAction(self.actionSave)
        self.menufile.addAction(self.actionExport)
        self.menuedit.addAction(self.actionfind)
        self.menuedit.addAction(self.actionFInd_replace)

        self.retranslateUi(ltx_editor)

        QMetaObject.connectSlotsByName(ltx_editor)
    # setupUi

    def retranslateUi(self, ltx_editor):
        ltx_editor.setWindowTitle(QCoreApplication.translate("ltx_editor", u"MainWindow", None))
        self.action_newproject.setText(QCoreApplication.translate("ltx_editor", u"New project", None))
        self.actionOpenProject.setText(QCoreApplication.translate("ltx_editor", u"Open project", None))
        self.actionfind.setText(QCoreApplication.translate("ltx_editor", u"Find in files", None))
        self.actionFInd_replace.setText(QCoreApplication.translate("ltx_editor", u"FInd & replace", None))
        self.actionExport.setText(QCoreApplication.translate("ltx_editor", u"Export", None))
        self.actionimport.setText(QCoreApplication.translate("ltx_editor", u"import", None))
        self.actionSave.setText(QCoreApplication.translate("ltx_editor", u"Save ", None))
        self.Recompile_btn.setText(QCoreApplication.translate("ltx_editor", u"Recompile", None))
        self.menufile.setTitle(QCoreApplication.translate("ltx_editor", u"file", None))
        self.menuedit.setTitle(QCoreApplication.translate("ltx_editor", u"edit", None))
        self.menuhelp.setTitle(QCoreApplication.translate("ltx_editor", u"help", None))
    # retranslateUi

