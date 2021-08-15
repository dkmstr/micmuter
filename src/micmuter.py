import sys
import typing

from PyQt5 import QtGui
from PyQt5 import QtWidgets

# Ensures that we have resources loaded
import muter


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    icon = muter.ui.setThemeAsOS(app, ':/images/icon-light.png', ':/images/icon-dark.png')

    # Create the tray icon
    tray = QtWidgets.QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setVisible(True)

    # Creating the options
    menu = QtWidgets.QMenu()
    configure = QtWidgets.QAction("Configure")
    configure.triggered.connect(lambda: muter.ui.config_window.ConfigWindow().exec_())

    # To quit the app
    quit = QtWidgets.QAction("Quit")
    quit.triggered.connect(app.quit)

    menu.addAction(configure) # Adding the configure option to the menu
    menu.addAction(quit)  # Adding the quit option to the menu

    # Adding options to the System Tray
    tray.setContextMenu(menu)

    app.exec_()


if __name__ == '__main__':
    main()
