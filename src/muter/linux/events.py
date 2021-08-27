import typing

HOTKEY_EVENT = None  # Not used in linux

def registerHotkey(handle: typing.Any, hotkey_id: int, hotkey_code: int, hotkey_modifiers: int) -> None:
    """
    Registers a hotkey for a window.
    """
    pass

def unregisterHotkey(handle: typing.Any, hotkey_id: int) -> None:
    """
    Unregisters a hotkey for a window.
    """
    pass

def as_event(data: typing.Any) -> typing.Any:
    return ''
    
