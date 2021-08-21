import sys
import typing

from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5 import QtCore


# Ensures that we have resources loaded
import muter

# for pyinstaller
import muter.ui.config_window
import muter.ui.micmuter_rc
import muter.ui.config_ui


class MicMuterWindow(QtWidgets.QMainWindow):
    tray: typing.Optional['MicMuterTray']
    audio: muter.system.sound.AudioUtilities

    def __init__(
        self,
        icon: QtGui.QIcon,
        flags: typing.Union[QtCore.Qt.WindowFlags, QtCore.Qt.WindowType],
    ) -> None:
        super().__init__(parent=None, flags=flags)
        self.setWindowTitle("Mic Muter")
        self.setWindowIcon(icon)
        self.setVisible(False)
        self.audio = muter.system.sound.AudioUtilities()
        self.audio.unMuteMicrophone()

    def nativeEvent(self, eventType, message) -> typing.Tuple[bool, int]:
        if eventType == "windows_generic_MSG":
            msg = muter.system.events.as_event(message)
            if msg.message == muter.system.events.HOTKEY_EVENT:
                self.toggle_mute()
        return super().nativeEvent(eventType, message)

    def setTray(self, tray: 'MicMuterTray'):
        self.tray = tray

    def unmute(self):
        self.audio.unMuteMicrophone()

    def toggle_mute(self) -> None:
        self.audio.toggleMute()
        if self.tray:
            if self.audio.is_muted:
                self.tray.setIcon(QtGui.QIcon(":/images/icon-red.png"))
            else:
                self.tray.setIcon(QtGui.QIcon(":/images/icon-green.png"))


class MicMuterTray(QtWidgets.QSystemTrayIcon):
    def __init__(
        self, icon: QtGui.QIcon, parent: typing.Optional[QtWidgets.QWidget] = None
    ):
        super().__init__(icon, parent)
        self.setVisible(True)
        # self.activated.connect(self.on_activated)

def main() -> None:
    try:
        # Include in try/except block if you're also targeting Mac/Linux
        from PyQt5.QtWinExtras import QtWin  # type: ignore
        myappid = 'dkmaster.micmuter.micmuter.1.0.0'
        QtWin.setCurrentProcessExplicitAppUserModelID(myappid)  # type: ignore
    except Exception:
        pass

    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    icon = muter.ui.setThemeAsOS(
        app, ':/images/icon-light.png', ':/images/icon-dark.png'
    )

    # Create the tray icon
    mainWindow = MicMuterWindow(icon, QtCore.Qt.WindowStaysOnTopHint)
    tray = MicMuterTray(QtGui.QIcon(":/images/icon-green.png"), parent=mainWindow)
    mainWindow.setTray(tray)

    # Register hotkey
    config = muter.settings.Settings.read()
    hotkey = config.hotkey

    if hotkey:
        muter.system.events.registerHotkey(mainWindow.winId(), 0x01, hotkey, 0)

    # Configure the application
    def doConfig() -> None:
        # Create the configuration window
        try:
            config = muter.ui.config_window.ConfigWindow(mainWindow)
            config.exec()
        except Exception as e:
            print(e)


    # Creating the options
    menu = QtWidgets.QMenu()
    configure = QtWidgets.QAction("Configure")
    configure.triggered.connect(doConfig)

    # To quit the app
    quit = QtWidgets.QAction("Quit")
    quit.triggered.connect(app.quit)

    menu.addAction(configure)  # Adding the configure option to the menu
    menu.addAction(quit)  # Adding the quit option to the menu

    # Adding options to the System Tray
    tray.setContextMenu(menu)

    app.exec_()

    mainWindow.unmute()


if __name__ == '__main__':
    main()
