import sys

from . import keycodes

if sys.platform == 'win32':
    from . import windows as system
else:
    from . import linux as system

