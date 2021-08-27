import sys
import os
import os.path
import pathlib

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    # frozen
    base_dir = sys._MEIPASS  # type: ignore
else:
    base_dir = str(pathlib.Path(os.path.dirname(os.path.abspath(__file__))).parent.absolute())

def play(sound: str):
    """
    Plays a sound file on linux
    """
    os.system(f'play {base_dir}/sounds/{sound}')

    

