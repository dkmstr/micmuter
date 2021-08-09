import sys

from PyQt5 import QtGui
from PyQt5 import QtWidgets

# Ensures that we have resources loaded
from muter.ui import micmuter_rc

app = QtWidgets.QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)

# Adding an icon
icon = QtGui.QIcon(':/images/icon.png')

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
