import typing

from PyQt5 import QtWidgets, QtGui

from muter import keycodes
from muter import settings

from . import config_ui


class ConfigWindow(QtWidgets.QDialog, config_ui.Ui_Configuration):
    config: settings.Settings

    def __init__(self, parent: typing.Optional[QtWidgets.QWidget] = None) -> None:
        from muter import system

        super(ConfigWindow, self).__init__(parent)
        self.config = settings.Settings.read()

        self.setupUi(self)

        self.buttonBox.accepted.connect(self.save_config)
        self.buttonBox.rejected.connect(self.close)

        if self.config.hotkey:
            self.hotKey.setText(keycodes.vk_name_keys[self.config.hotkey].upper())
            # Unregister the hotkey while the window is open
            system.events.unregisterHotkey(self.parent().winId(), 0x01)

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        vk = a0.nativeVirtualKey()
        if vk in keycodes.vk_name_keys:
            self.hotKey.setText(keycodes.vk_name_keys[vk].upper())
            self.config = self.config._replace(hotkey=vk)
        else:
            self.hotKey.setText(str(vk))
        return super().keyPressEvent(a0)

    def save_config(self):
        from muter import system

        self.config.save()
        self.close()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        from muter import system

        system.events.registerHotkey(self.parent().winId(), 0x01, self.config.hotkey, 0)
        return super().closeEvent(a0)
