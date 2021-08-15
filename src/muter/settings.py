import typing

from PyQt5 import QtCore

settings = QtCore.QSettings('Dkmaster', 'MicMuter')

class Settings(typing.NamedTuple):
    """
    Settings for the muter
    """
    device: str
    hotkey: str

    @staticmethod
    def read(self) -> 'Settings':
        """
        Create a Settings object from a QSettings object
        """
        return Settings(
            settings.value('device', type=str),
            settings.value('hotkey', type=str)
        )

    def save(self) -> None:
        """
        Save the settings to a QSettings object
        """
        settings.setValue('device', self.device)
        settings.setValue('hotkey', self.hotkey)

