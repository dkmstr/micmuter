from PySide2 import QtGui
from PySide2 import QtWidgets
from PySide2 import QtCore

from . import micmuter_rc
from . import micmuter_ui

def setThemeAsOS(app: QtWidgets.QApplication) -> None:
    # Import system
    from muter import system

    # If dark theme is enabled, set the style and update icon to dark one
    if system.usesDarkTheme():
        app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))  # type: ignore
        darkPalette = QtGui.QPalette()
        darkColor = QtGui.QColor(45, 45, 45)
        disabledColor = QtGui.QColor(127, 127, 127)
        darkPalette.setColor(QtGui.QPalette.Window, darkColor)
        darkPalette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
        darkPalette.setColor(QtGui.QPalette.Base, QtGui.QColor(18, 18, 18))
        darkPalette.setColor(QtGui.QPalette.AlternateBase, darkColor)
        darkPalette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
        darkPalette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
        darkPalette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
        darkPalette.setColor(
            QtGui.QPalette.Disabled, QtGui.QPalette.Text, disabledColor
        )
        darkPalette.setColor(QtGui.QPalette.Button, darkColor)
        darkPalette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
        darkPalette.setColor(
            QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, disabledColor
        )
        darkPalette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)
        darkPalette.setColor(QtGui.QPalette.Link, QtGui.QColor(42, 130, 218))
        darkPalette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(42, 130, 218))
        darkPalette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)
        darkPalette.setColor(
            QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, disabledColor
        )

        app.setPalette(darkPalette)

        app.setStyleSheet(
            'QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }'
        )
