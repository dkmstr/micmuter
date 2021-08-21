import typing

# Windows libs
import win32gui
import win32con
import ctypes

HOTKEY_EVENT = win32con.WM_HOTKEY

def registerHotkey(handle: typing.Any, hotkey_id: int, hotkey_code: int, hotkey_modifiers: int) -> None:
    """
    Registers a hotkey for a window.
    """
    win32gui.RegisterHotKey(handle, hotkey_id, hotkey_modifiers, hotkey_code)

def as_event(data: typing.Any) -> ctypes.wintypes.MSG:
    return ctypes.wintypes.MSG.from_address(data.__int__())
