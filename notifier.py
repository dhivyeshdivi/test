from plyer import notification
import subprocess
import platform

class Notifier:
    def notify(self, message):
        """Send a local notification."""
        notification.notify(
            title="Class Monitor Alert",
            message=message,
            timeout=5
        )

    def check_network(self, host="8.8.8.8", threshold=100):
        """Check network stability by pinging a host and measuring latency."""
        try:
            if platform.system().lower() == "windows":
                result = subprocess.run(["ping", "-n", "1", host], capture_output=True, text=True)
            else:
                result = subprocess.run(["ping", "-c", "1", host], capture_output=True, text=True)
                # Extract latency (basic parsing)
                output = result.stdout
                if "time=" in output:
                    latency = float(output.split("time=")[1].split(" ")[0])
                    return latency < threshold  # True if stable
            return False
        except Exception as e:
            print(f"Network check error: {e}")
            return False