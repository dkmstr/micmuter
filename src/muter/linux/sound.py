import typing
import logging

import alsaaudio


logger = logging.getLogger(__name__)


class AudioUtilities:
    mics: typing.List[alsaaudio.Mixer]

    # Constructor
    def __init__(self):
        self.is_muted = False
        self.mics = []
        # Look for cards
        for card in alsaaudio.card_indexes():
            # Locate Capture devices if exists
            if 'Capture' in alsaaudio.mixers(card):
                mixer = alsaaudio.Mixer(cardindex=card, control='Capture')
                # Check if device is muteable
                if any(map(mixer.switchcap().__contains__,  ['Capture Mute', 'Joined Capture Mute'])):
                    self.mics.append(mixer)  # It is, add to mic list

    def setMicrophoneMuted(self, muted: bool) -> None:
        self.is_muted = muted
        for mic in self.mics:
            try:
                mic.setrec(not muted)  # 0 = mute, 1 = unmute
            except Exception as e:
                logger.error('EXCEPTION [setMic]: %s', e)

    def muteMicrophone(self) -> None:
        self.setMicrophoneMuted(True)

    def unMuteMicrophone(self) -> None:
        self.setMicrophoneMuted(False)

    # Call this function to mute if is_muted = False, otherwise it'll unmute the mics
    def toggleMute(self):
        self.setMicrophoneMuted(not self.is_muted)
