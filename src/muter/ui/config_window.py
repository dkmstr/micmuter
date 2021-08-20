import typing

from PyQt5 import QtWidgets, QtGui

from muter import keycodes
from muter import settings

from . import config_ui


class ConfigWindow(QtWidgets.QDialog, config_ui.Ui_Configuration):
    config: settings.Settings
    def __init__(self, parent: typing.Optional[QtWidgets.QWidget] = None, icon: typing.Optional[QtGui.QIcon] = None) -> None:
        super(ConfigWindow, self).__init__(parent)
        self.config = settings.Settings.read()
        self.setupUi(self)

        self.buttonBox.accepted.connect(self.save_config)
        self.buttonBox.rejected.connect(self.close)
        if icon:
            self.setWindowIcon(icon)

        if self.config.hotkey:
            self.hotKey.setText(keycodes.vk_name_keys[self.config.hotkey].upper())

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        vk = a0.nativeVirtualKey()
        if vk in keycodes.vk_name_keys:
            self.hotKey.setText(keycodes.vk_name_keys[vk].upper())
            self.config = self.config._replace(hotkey=vk)
        else:
            self.hotKey.setText(str(vk))
        return super().keyPressEvent(a0)

    def save_config(self):
        self.config.save()

        self.close()
