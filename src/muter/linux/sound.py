import typing
import logging

from pyalsa import alsamixer
from pyalsa import alsacard

logger = logging.getLogger(__name__)

class AudioUtilities:
    mixers: typing.List[alsamixer.Mixer]
    mics: typing.List[alsamixer.Element]

    # Constructor
    def __init__(self):
        self.is_muted = False
        self.mixers = [
            self._getAlsaMixer(f'hw:{i}') for i in alsacard.card_list()
        ]
        # Look for mics
        self.mics = list(self._getAlsaMics())


    def _getAlsaMixer(self, mixer_name: str) -> alsamixer.Mixer:
        mixer = alsamixer.Mixer()
        mixer.attach(mixer_name)
        mixer.load()
        return mixer

    def _getAlsaMics(self) -> typing.Iterable[alsamixer.Element]:
        for mixer in self.mixers:
            for name, index in mixer.list():
                if name == 'Capture':
                    mic = alsamixer.Element(mixer=mixer, name=name, index=index)
                    # If it can be captured and is mutable
                    if mic.has_channel(0, True) and mic.has_switch(True):
                        yield mic

    def setMicrophoneMuted(self, muted: bool) -> None:
        for mic in self.mics:
            try:
                mic.set_switch_all(not muted, True)
            except Exception as e:
                logger.error('EXCEPTION [setMic]: %s', e)

    def muteMicrophone(self) -> None:
        self.setMicrophoneMuted(True)
        self.is_muted = True

    def unMuteMicrophone(self) -> None:
        self.setMicrophoneMuted(False)
        self.is_muted = False

    # Call this function to mute if is_muted = False, otherwise it'll unmute the mics
    def toggleMute(self):
        if self.is_muted == False:
            self.muteMicrophone()
        else:
            self.unMuteMicrophone()
