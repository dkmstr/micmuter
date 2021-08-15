import sys

from . import keycodes
from . import ui
from . import settings

if sys.platform == 'win32':
    from . import windows as system
else:
    from . import linux as system

