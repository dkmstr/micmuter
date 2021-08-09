import typing

# Windows libs
import win32api

__all__ = ['isKeyPressed']

# Get if key is pressed
def isKeyPressed(key: int) -> bool:
    return win32api.GetAsyncKeyState(key) & 0x8000
