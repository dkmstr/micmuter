import sys

from . import keycodes
from . import ui
from . import settings
from . import alert

if sys.platform == "win32":
    from . import windows as system
elif sys.platform == "linux":
    from . import linux as system
elif sys.platform == "darwin":
    #from . import macos as system
    pass

