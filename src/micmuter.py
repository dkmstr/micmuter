import sys

from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5 import QtCore

# Ensures that we have resources loaded
from muter.ui import micmuter_rc

import muter

def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    icon = QtGui.QIcon(':/images/icon-light.png')

    # If dark theme is enabled, set the style sheet
    if muter.system.usesDarkTheme():
        app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        darkPalette = QtGui.QPalette()
        darkColor = QtGui.QColor(45,45,45)
        disabledColor = QtGui.QColor(127,127,127)
        darkPalette.setColor(QtGui.QPalette.Window, darkColor)
        darkPalette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
        darkPalette.setColor(QtGui.QPalette.Base, QtGui.QColor(18,18,18))
        darkPalette.setColor(QtGui.QPalette.AlternateBase, darkColor)
        darkPalette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
        darkPalette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
        darkPalette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
        darkPalette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.Text, disabledColor)
        darkPalette.setColor(QtGui.QPalette.Button, darkColor)
        darkPalette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
        darkPalette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, disabledColor)
        darkPalette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)
        darkPalette.setColor(QtGui.QPalette.Link, QtGui.QColor(42, 130, 218))
        darkPalette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(42, 130, 218))
        darkPalette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)
        darkPalette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, disabledColor)

        app.setPalette(darkPalette)

        app.setStyleSheet('QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }')
        icon = QtGui.QIcon(':/images/icon-dark.png')


    # Adding item on the menu bar
    tray = QtWidgets.QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setVisible(True)

    # Creating the options
    menu = QtWidgets.QMenu()
    configure = QtWidgets.QAction("Configure")

    # To quit the app
    quit = QtWidgets.QAction("Quit")
    quit.triggered.connect(app.quit)

    menu.addAction(configure)
    menu.addAction(quit)

    # Adding options to the System Tray
    tray.setContextMenu(menu)

    app.exec_()


if __name__ == '__main__':
    main()