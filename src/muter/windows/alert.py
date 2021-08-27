import sys
import os.path
import pathlib
import winsound

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    # frozen
    base_dir = sys._MEIPASS  # type: ignore
else:
    base_dir = str(pathlib.Path(os.path.dirname(os.path.abspath(__file__))).parent.absolute())

def play(sound: str):
    winsound.PlaySound(os.path.join(base_dir, 'sounds', sound), winsound.SND_ASYNC)

