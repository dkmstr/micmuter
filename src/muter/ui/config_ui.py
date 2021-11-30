# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'config.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QVBoxLayout, QWidget)
from  . import micmuter_rc

class Ui_Configuration(object):
    def setupUi(self, Configuration):
        if not Configuration.objectName():
            Configuration.setObjectName(u"Configuration")
        Configuration.setWindowModality(Qt.ApplicationModal)
        Configuration.resize(174, 89)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Configuration.sizePolicy().hasHeightForWidth())
        Configuration.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/images/icon-light.png", QSize(), QIcon.Normal, QIcon.Off)
        Configuration.setWindowIcon(icon)
        Configuration.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.verticalLayout = QVBoxLayout(Configuration)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.hotkey = QWidget(Configuration)
        self.hotkey.setObjectName(u"hotkey")
        self.hotkey.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.horizontalLayout_2 = QHBoxLayout(self.hotkey)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.hotkey)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.hotKey = QLineEdit(self.hotkey)
        self.hotKey.setObjectName(u"hotKey")
        self.hotKey.setFrame(True)
        self.hotKey.setAlignment(Qt.AlignCenter)
        self.hotKey.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.hotKey)


        self.verticalLayout.addWidget(self.hotkey)

        self.buttonBox = QDialogButtonBox(Configuration)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Configuration)

        QMetaObject.connectSlotsByName(Configuration)
    # setupUi

    def retranslateUi(self, Configuration):
        Configuration.setWindowTitle(QCoreApplication.translate("Configuration", u"Configuration", None))
        self.label.setText(QCoreApplication.translate("Configuration", u"Hotkey", None))
        self.hotKey.setPlaceholderText(QCoreApplication.translate("Configuration", u"Press a key to assign the hot key", None))
    # retranslateUi

