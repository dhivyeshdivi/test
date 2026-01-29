import librosa
import numpy as np

class SilenceDetector:
    def __init__(self, threshold=0.01, silence_duration=10, sample_rate=44100):
        self.threshold = threshold  # RMS threshold for silence
        self.silence_duration = silence_duration
        self.sample_rate = sample_rate
        self.silence_counter = 0

    def is_silent(self, audio_data):
        """Check if audio is silent based on RMS."""
        rms = np.sqrt(np.mean(audio_data**2))
        if rms < self.threshold:
            self.silence_counter += len(audio_data) / self.sample_rate
            if self.silence_counter >= self.silence_duration:
                self.silence_counter = 0  # Reset after detection
                return True
        else:
            self.silence_counter = 0
        return False