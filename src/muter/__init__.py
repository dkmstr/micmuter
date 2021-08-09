import sys

from . import keycodes
from . import ui

if sys.platform == 'win32':
    from . import windows as system
else:
    from . import linux as system

