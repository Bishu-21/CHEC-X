from glob import glob
import cv2
import mediapipe as mp
import numpy as np
import threading as th

# Placeholders and global variables
x = 0  # X-axis head pose
y = 0  # Y-axis head pose
X_AXIS_CHEAT = 0
Y_AXIS_CHEAT = 0

def pose():
    global x, y, X_AXIS_CHEAT, Y_AXIS_CHEAT
    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)
    cap = cv2.VideoCapture(0)
    mp_drawing = mp.solutions.drawing_utils

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            break
        
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = face_mesh.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        img_h, img_w, _ = image.shape
        face_3d, face_2d = [], []
        face_ids = [33, 263, 1, 61, 291, 199]

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                mp_drawing.draw_landmarks(
                    image=image,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_CONTOURS,
                    landmark_drawing_spec=None)
                
                for idx, lm in enumerate(face_landmarks.landmark):
                    if idx in face_ids:
                        if idx == 1:
                            nose_2d = (lm.x * img_w, lm.y * img_h)
                            nose_3d = (lm.x * img_w, lm.y * img_h, lm.z * 8000)
                        
                        x, y = int(lm.x * img_w), int(lm.y * img_h)
                        face_2d.append([x, y])
                        face_3d.append([x, y, lm.z])
                
                face_2d = np.array(face_2d, dtype=np.float64)
                face_3d = np.array(face_3d, dtype=np.float64)
                focal_length = img_w
                cam_matrix = np.array([[focal_length, 0, img_h / 2],
                                       [0, focal_length, img_w / 2],
                                       [0, 0, 1]])
                dist_matrix = np.zeros((4, 1), dtype=np.float64)

                success, rot_vec, trans_vec = cv2.solvePnP(face_3d, face_2d, cam_matrix, dist_matrix)
                rmat, _ = cv2.Rodrigues(rot_vec)
                angles, _, _, _, _, _ = cv2.RQDecomp3x3(rmat)
                x, y = angles[0] * 360, angles[1] * 360
                
                if y < -10:
                    text = "Looking Left"
                elif y > 10:
                    text = "Looking Right"
                elif x < -10:
                    text = "Looking Down"
                else:
                    text = "Forward"
                text = f"{int(x)}::{int(y)} {text}"
                
                X_AXIS_CHEAT = 1 if abs(y) > 10 else 0
                Y_AXIS_CHEAT = 1 if x < -5 else 0

                nose_3d_projection, _ = cv2.projectPoints(nose_3d, rot_vec, trans_vec, cam_matrix, dist_matrix)
                p1, p2 = (int(nose_2d[0]), int(nose_2d[1])), (int(nose_3d_projection[0][0][0]), int(nose_3d_projection[0][0][1]))
                
                cv2.putText(image, text, (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        
        cv2.imshow('Head Pose Estimation', image)
        if cv2.waitKey(5) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    t1 = th.Thread(target=pose)
    t1.start()
    t1.join()
