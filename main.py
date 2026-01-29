import threading
import time
import signal
import sys
from audio_recorder_streamlit import AudioRecorder
from silence_detector import SilenceDetector
from notifier import Notifier

# Global flag to control monitoring
monitoring = True

def monitor_loop():
    recorder = AudioRecorder()
    detector = SilenceDetector(threshold=0.01, silence_duration=10)
    notifier = Notifier()
    while monitoring:
        # Record and analyze
        audio_data = recorder.record_chunk(duration=1)
        is_silent = detector.is_silent(audio_data)
        network_status = notifier.check_network()
        # Notify on issues
        if is_silent:
            notifier.notify("Silence detected in class - check audio and interact with students!")
        if not network_status:
            notifier.notify("Network instability detected - check connection!")
        time.sleep(1)

def signal_handler(sig, frame):
    global monitoring
    print("Stopping background monitoring...")
    monitoring = False
    sys.exit(0)

if __name__ == '__main__':
    # Handle Ctrl+C to stop gracefully
    signal.signal(signal.SIGINT, signal_handler)
    print("Starting background monitoring. Press Ctrl+C to stop.")
    # Run in a daemon thread (background)
    thread = threading.Thread(target=monitor_loop, daemon=True)
    thread.start()
    # Keep the main thread alive
    while True:
        time.sleep(1)