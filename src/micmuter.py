import sys
import typing

from PySide2 import QtWidgets, QtGui, QtCore


# Ensures that we have resources loaded
import muter


class MicMuterWindow(QtWidgets.QMainWindow, muter.ui.micmuter_ui.Ui_mainWindow):
    tray: typing.Optional['MicMuterTray']
    app: QtWidgets.QApplication
    audio: muter.system.sound.AudioUtilities
    config: muter.settings.Settings
    capturing: bool

    def __init__(
        self,
        app: QtWidgets.QApplication,
    ) -> None:
        super().__init__()
        self.app = app

        self.setupUi(self)

        self.config = muter.settings.Settings.read()
        self.capturing = False

        self.audio = muter.system.sound.AudioUtilities()
        self.audio.unMuteMicrophone()

        if self.config.hotkey:
            self.hotKey.setText(muter.keycodes.vk_name_keys[self.config.hotkey].upper())

        self.setHotkeyButton.clicked.connect(self.activateHotkeyCapture)
        self.actionQuit.triggered.connect(self.app.quit)
        self.actionMinimizeToTray.triggered.connect(self.close)

    def nativeEvent(self, eventType, message) -> typing.Tuple:
        try:
            if self.tray and eventType == "windows_generic_MSG":
                msg = muter.system.events.as_event(message)
                if msg.message == muter.system.events.HOTKEY_EVENT:
                    self.toggle_mute()
        except Exception:
            pass
        return super().nativeEvent(eventType, message)

    def closeEvent(self, event: QtCore.QEvent) -> None:
        event.ignore()
        self.hide()
        self.trayMessage('Mic muter running on background')

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        if self.capturing:
            self.hotKey.setStyleSheet('')
            self.capturing = False
            vk = a0.nativeVirtualKey()
            if vk in muter.keycodes.vk_name_keys:
                self.hotKey.setText(muter.keycodes.vk_name_keys[vk].upper())
                self.config = self.config._replace(hotkey=vk)
                muter.system.events.registerHotkey(
                    self.winId(), 0x01, self.config.hotkey, 0
                )
                self.config.save()
            else:
                self.hotKey.setText(str(vk))
        else:
            super().keyPressEvent(a0)

    def activateHotkeyCapture(self):
        self.capturing = True
        muter.system.events.unregisterHotkey(self.winId(), 0x01)
        self.hotKey.setStyleSheet('color: red')
        self.hotKey.setText('Capturing, press a key...')

    def trayMessage(self, message: str, timeout: int = 500) -> None:
        if self.tray:
            self.tray.showMessage('Mic Muter', message, self.tray.icon(), timeout)

    def setTray(self, tray: 'MicMuterTray'):
        self.tray = tray

    def unmute(self):
        self.audio.unMuteMicrophone()

    def toggle_mute(self) -> None:
        self.audio.toggleMute()
        if self.tray:
            if self.audio.is_muted:
                muter.alert.play('off.wav')
                self.tray.setIcon(QtGui.QIcon(":/images/icon-red.png"))
                self.trayMessage('Microphone muted')
            else:
                muter.alert.play('on.wav')
                self.tray.setIcon(QtGui.QIcon(":/images/icon-green.png"))
                self.trayMessage('Microphone unmuted')


class MicMuterTray(QtWidgets.QSystemTrayIcon):
    def __init__(
        self, icon: QtGui.QIcon, parent: typing.Optional[QtWidgets.QWidget] = None
    ):
        super().__init__(icon, parent)
        self.setVisible(True)
        self.activated.connect(self.checkShow)

    def checkShow(self, reason: QtWidgets.QSystemTrayIcon.ActivationReason) -> None:
        if reason == QtWidgets.QSystemTrayIcon.DoubleClick:
            self.parent().show()


def main() -> None:
    try:
        from PySide2.QtWinExtras import QtWin  # type: ignore

        myappid = 'dkmaster.micmuter.micmuter.1.0.0'
        QtWin.setCurrentProcessExplicitAppUserModelID(myappid)  # type: ignore
    except Exception:
        pass  # linux or mac will reach this, but this app is for windows mainly right now...

    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    muter.ui.setThemeAsOS(app)

    # Create the tray icon
    mainWindow = MicMuterWindow(app)
    tray = MicMuterTray(QtGui.QIcon(":/images/icon-green.png"), parent=mainWindow)
    mainWindow.setTray(tray)

    # Register hotkey
    config = muter.settings.Settings.read()
    hotkey = config.hotkey

    if hotkey:
        muter.system.events.registerHotkey(mainWindow.winId(), 0x01, hotkey, 0)

    # Creating the options
    menu = QtWidgets.QMenu()
    configure = QtWidgets.QAction("Configure")
    configure.triggered.connect(lambda: mainWindow.show())

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
