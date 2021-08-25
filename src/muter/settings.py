import typing

from PySide2 import QtCore

settings = QtCore.QSettings('Dkmaster', 'MicMuter')

class Settings(typing.NamedTuple):
    """
    Settings for the muter
    """
    hotkey: int = 0

    @staticmethod
    def read() -> 'Settings':
        """
        Create a Settings object from a QSettings object
        """
        return Settings(
            typing.cast(int, settings.value('hotkey', type=int))
        )

    def save(self) -> None:
        """
        Save the settings to a QSettings object
        """
        settings.setValue('hotkey', self.hotkey)

