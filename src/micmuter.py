import sys
import ctypes
import typing

from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5 import QtCore


# Ensures that we have resources loaded
import muter

audio = muter.system.sound.AudioUtilities()

class MicMuterWindow(QtWidgets.QMainWindow):
    def __init__(
        self,
        icon: QtGui.QIcon,
        flags: typing.Union[QtCore.Qt.WindowFlags, QtCore.Qt.WindowType],
    ) -> None:
        super().__init__(parent=None, flags=flags)
        self.setWindowTitle("Mic Muter")
        self.setWindowIcon(icon)
        self.setVisible(False)
        audio.unMuteMicrophone()

    def nativeEvent(self, eventType, message) -> typing.Tuple[bool, int]:
        if eventType == "windows_generic_MSG":
            msg = muter.system.events.as_event(message)
            if msg.message == muter.system.events.HOTKEY_EVENT:
                self.toggle_mute()
        return super().nativeEvent(eventType, message)

    def toggle_mute(self) -> None:
        print('Toggling mute')
        audio.toggleMute()



class MicMuterTray(QtWidgets.QSystemTrayIcon):
    def __init__(self, icon: QtGui.QIcon, parent: typing.Optional[QtWidgets.QWidget] = None):
        super().__init__(icon, parent)
        self.setVisible(True)
        # self.activated.connect(self.on_activated)



def main() -> None:
    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    icon = muter.ui.setThemeAsOS(
        app, ':/images/icon-light.png', ':/images/icon-dark.png'
    )

    # Create the tray icon
    mainWindow = MicMuterWindow(icon, QtCore.Qt.WindowStaysOnTopHint)
    tray = MicMuterTray(icon, parent=mainWindow)

    # Register hotkey
    config = muter.settings.Settings.read()
    hotkey = config.hotkey
    if hotkey:
        muter.system.events.registerHotkey(mainWindow.winId(), hotkey, hotkey, 0)

    # Creating the options
    menu = QtWidgets.QMenu()
    configure = QtWidgets.QAction("Configure")
    configure.triggered.connect(lambda: muter.ui.config_window.ConfigWindow(mainWindow, icon=icon).exec_())

    # To quit the app
    quit = QtWidgets.QAction("Quit")
    quit.triggered.connect(app.quit)

    menu.addAction(configure)  # Adding the configure option to the menu
    menu.addAction(quit)  # Adding the quit option to the menu

    # Adding options to the System Tray
    tray.setContextMenu(menu)

    app.exec_()


if __name__ == '__main__':
    main()
