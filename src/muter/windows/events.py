import typing

# Windows libs
import win32con
import ctypes
import ctypes.wintypes

user32 = ctypes.windll.user32

HOTKEY_EVENT = win32con.WM_HOTKEY

def registerHotkey(handle: typing.Any, hotkey_id: int, hotkey_code: int, hotkey_modifiers: int) -> None:
    """
    Registers a hotkey for a window.
    """
    user32.RegisterHotKey(int(handle), hotkey_id, hotkey_modifiers, hotkey_code)
    # win32gui.RegisterHotKey(handle, hotkey_id, hotkey_modifiers, hotkey_code)

def unregisterHotkey(handle: typing.Any, hotkey_id: int) -> None:
    """
    Unregisters a hotkey for a window.
    """
    user32.UnregisterHotKey(int(handle), hotkey_id)
    # win32gui.UnregisterHotKey(handle, hotkey_id)

def as_event(data: typing.Any) -> ctypes.wintypes.MSG:
    return ctypes.wintypes.MSG.from_address(data.__int__())
