import sounddevice as sd
import numpy as np

class AudioRecorder:
    def __init__(self, sample_rate=44100, channels=1):
        self.sample_rate = sample_rate
        self.channels = channels

    def record_chunk(self, duration=1):
        """Record a chunk of audio for the given duration."""
        recording = sd.rec(int(duration * self.sample_rate), samplerate=self.sample_rate, channels=self.channels, dtype='float32')
        sd.wait()
        return recording.flatten()  # Return as 1D numpy array