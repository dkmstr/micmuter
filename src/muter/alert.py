import os.path
import winsound


def play(sound: str):
    winsound.PlaySound(os.path.join('sounds', sound), winsound.SND_ASYNC)

