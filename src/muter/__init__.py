import sys

from . import keycodes

if sys.platform == 'win32':
    from windows import keys
else:
    from linux import keys
