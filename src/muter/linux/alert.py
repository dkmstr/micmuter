import sys
import os
import os.path
import pathlib
import wave
import logging

import alsaaudio

logger = logging.getLogger(__name__)

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    # frozen
    base_dir = sys._MEIPASS  # type: ignore
else:
    base_dir = str(
        pathlib.Path(os.path.dirname(os.path.abspath(__file__))).parent.parent.absolute()
    )


def play(sound: str) -> None:
    """
    Plays a sound file on linux
    """
    format = None
    with wave.open(os.path.join(base_dir, 'sounds', sound), 'rb') as f:
        # 8bit is unsigned in wav files
        if f.getsampwidth() == 1:
            format = alsaaudio.PCM_FORMAT_U8
        # Otherwise we assume signed data, little endian
        elif f.getsampwidth() == 2:
            format = alsaaudio.PCM_FORMAT_S16_LE
        elif f.getsampwidth() == 3:
            format = alsaaudio.PCM_FORMAT_S24_3LE
        elif f.getsampwidth() == 4:
            format = alsaaudio.PCM_FORMAT_S32_LE
        else:
            raise ValueError('Unsupported format')

        periodsize = f.getframerate() // 8

        logger.debug(
            '%d channels, %d sampling rate, format %d, periodsize %d\n'
            % (f.getnchannels(), f.getframerate(), format, periodsize)
        )

        device = alsaaudio.PCM(device='default')
        device.setchannels(f.getnchannels())
        device.setrate(f.getframerate())
        device.setformat(format)
        device.setperiodsize(periodsize)

        data = f.readframes(periodsize)
        while data:
            device.write(data)
            data = f.readframes(periodsize)
