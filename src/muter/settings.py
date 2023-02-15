import typing

from PySide6 import QtCore

settings = QtCore.QSettings('Dkmaster', 'MicMuter')

class Settings(typing.NamedTuple):
    """
    Settings for the muter
    """
    hotkey: int = 0
    clipWait: int = 0

    @staticmethod
    def read() -> 'Settings':
        """
        Create a Settings object from a QSettings object
        """
        return Settings(
            typing.cast(int, settings.value('hotkey', type=int)),
            typing.cast(int, settings.value('clipWait', defaultValue=60, type=int)),
        )

    def save(self) -> None:
        """
        Save the settings to a QSettings object
        """
        settings.setValue('hotkey', self.hotkey)
        settings.setValue('clipWait', self.clipWait)


