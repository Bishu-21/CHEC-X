import sounddevice as sd
import numpy as np
import signal
import time

running = True

def signal_handler(sig, frame):
    global running
    running = False
    print("\n[INFO] Stopping Audio Processing...")

signal.signal(signal.SIGINT, signal_handler)

def sound():
    global running
    def callback(indata, frames, time, status):
        if status:
            print(status)
        volume_norm = np.linalg.norm(indata) * 10
        print(f"Sound Level: {volume_norm:.2f}")

    try:
        with sd.InputStream(callback=callback):
            print("[INFO] Audio Processing Started. Press Ctrl+C to stop.")
            while running:
                time.sleep(0.1)  # Reduce CPU usage

    except KeyboardInterrupt:
        print("\n[INFO] Keyboard Interrupt received. Exiting gracefully.")
    except Exception as e:
        print(f"[ERROR] An error occurred: {e}")

    print("[INFO] Audio Processing Stopped.")

if __name__ == "__main__":
    sound()
