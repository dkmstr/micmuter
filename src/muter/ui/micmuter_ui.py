# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'micmuter.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)
from  . import micmuter_rc

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(305, 121)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMaximumSize(QSize(320, 200))
        icon = QIcon()
        icon.addFile(u":/images/icon-light.png", QSize(), QIcon.Normal, QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.actionQuit = QAction(mainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionMinimizeToTray = QAction(mainWindow)
        self.actionMinimizeToTray.setObjectName(u"actionMinimizeToTray")
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.hkey_frame = QWidget(self.centralwidget)
        self.hkey_frame.setObjectName(u"hkey_frame")
        self.horizontalLayout_2 = QHBoxLayout(self.hkey_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.setHotkeyButton = QPushButton(self.hkey_frame)
        self.setHotkeyButton.setObjectName(u"setHotkeyButton")

        self.horizontalLayout_2.addWidget(self.setHotkeyButton)

        self.hotKey = QLineEdit(self.hkey_frame)
        self.hotKey.setObjectName(u"hotKey")
        self.hotKey.setMinimumSize(QSize(197, 0))
        self.hotKey.setFrame(True)
        self.hotKey.setAlignment(Qt.AlignCenter)
        self.hotKey.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.hotKey)


        self.verticalLayout.addWidget(self.hkey_frame)

        self.waitClip_frame = QHBoxLayout()
        self.waitClip_frame.setObjectName(u"waitClip_frame")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.waitClip_frame.addWidget(self.label)

        self.clipWait = QSpinBox(self.centralwidget)
        self.clipWait.setObjectName(u"clipWait")
        self.clipWait.setMinimumSize(QSize(197, 0))

        self.waitClip_frame.addWidget(self.clipWait)


        self.verticalLayout.addLayout(self.waitClip_frame)

        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 305, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        mainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionMinimizeToTray)
        self.menuFile.addAction(self.actionQuit)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Mic Muter", None))
        self.actionQuit.setText(QCoreApplication.translate("mainWindow", u"Quit", None))
        self.actionMinimizeToTray.setText(QCoreApplication.translate("mainWindow", u"Minimize", None))
        self.setHotkeyButton.setText(QCoreApplication.translate("mainWindow", u"Set Hotkey", None))
        self.hotKey.setPlaceholderText(QCoreApplication.translate("mainWindow", u"Press a key to assign the hot key", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"Clipboard Wait", None))
        self.menuFile.setTitle(QCoreApplication.translate("mainWindow", u"File", None))
    # retranslateUi

