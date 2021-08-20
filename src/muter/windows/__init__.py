from PyQt5 import QtCore

THEME_KEY = 'HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize'
LIGHT_VALUE = 'AppsUseLightTheme'

# Return if windows is configured with dark theme
def usesDarkTheme() -> bool:
    return QtCore.QSettings(THEME_KEY,QtCore.QSettings.NativeFormat).value(LIGHT_VALUE) == 0

from . import keys
from . import sound
