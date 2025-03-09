import audio
import head_pose
import detection
import threading as th

def run_thread(target_func, name):
    try:
        target_func()
    except Exception as e:
        print(f"Error in {name}: {e}")

if __name__ == "__main__":
    # Creating threads
    head_pose_thread = th.Thread(target=run_thread, args=(head_pose.pose, "Head Pose"))
    audio_thread = th.Thread(target=run_thread, args=(audio.sound, "Audio"))
    detection_thread = th.Thread(target=run_thread, args=(detection.run_detection, "Detection"))

    # Starting threads
    head_pose_thread.start()
    audio_thread.start()
    detection_thread.start()

    # Waiting for threads to complete
    head_pose_thread.join()
    audio_thread.join()
    detection_thread.join()
