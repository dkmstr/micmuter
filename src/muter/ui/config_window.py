import typing

from PyQt5 import QtWidgets
import sounddevice

from . import config_ui

class ConfigWindow(QtWidgets.QDialog, config_ui.Ui_Configuration):
    def __init__(self, parent: typing.Optional[QtWidgets.QWidget] = None):
        super(ConfigWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.buttonBox.accepted.connect(self.save_config)
        self.buttonBox.rejected.connect(self.close)

    def save_config(self):
        pass
