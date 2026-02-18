import cv2
import mediapipe as mp
import numpy as np

# Initialize Mediapipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7,
                       min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(1)

canvas = None
draw_color = (255, 0, 0)  # Default Blue
brush_thickness = 7
eraser_thickness = 40

xp, yp = 0, 0


def fingers_up(hand_landmarks):
    fingers = []

    # Thumb
    if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other four fingers
    tips = [8, 12, 16, 20]
    for tip in tips:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers


while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)

    if canvas is None:
        canvas = np.zeros_like(img)

    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    # ================= UI Buttons =================
    cv2.rectangle(img, (0, 0), (100, 60), (255, 0, 0), -1)
    cv2.rectangle(img, (110, 0), (210, 60), (0, 255, 0), -1)
    cv2.rectangle(img, (220, 0), (320, 60), (0, 0, 255), -1)
    cv2.rectangle(img, (330, 0), (430, 60), (0, 0, 0), -1)
    cv2.rectangle(img, (440, 0), (580, 60), (0, 255, 255), -1)

    cv2.putText(img, "BLUE", (15, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(img, "GREEN", (120, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(img, "RED", (240, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(img, "ERASER", (340, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(img, "CLEAR", (470, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
    # ==============================================

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            h, w, c = img.shape
            lm = handLms.landmark

            x1, y1 = int(lm[8].x * w), int(lm[8].y * h)   # Index finger
            x2, y2 = int(lm[12].x * w), int(lm[12].y * h) # Middle finger

            fingers = fingers_up(handLms)

            # ================= Selection Mode =================
            if fingers[1] and fingers[2]:
                xp, yp = 0, 0

                if y1 < 60:
                    if 0 < x1 < 100:
                        draw_color = (255, 0, 0)   # Blue
                    elif 110 < x1 < 210:
                        draw_color = (0, 255, 0)   # Green
                    elif 220 < x1 < 320:
                        draw_color = (0, 0, 255)   # Red
                    elif 330 < x1 < 430:
                        draw_color = (0, 0, 0)     # Eraser
                    elif 440 < x1 < 580:
                        canvas = np.zeros_like(img)  # Clear

                cv2.rectangle(img, (x1, y1 - 25),
                              (x2, y2 + 25),
                              draw_color, cv2.FILLED)

            # ================= Drawing Mode =================
            elif fingers[1] and not fingers[2]:

                cv2.circle(img, (x1, y1), 10,
                           draw_color, cv2.FILLED)

                if xp == 0 and yp == 0:
                    xp, yp = x1, y1

                thickness = eraser_thickness if draw_color == (0, 0, 0) else brush_thickness

                cv2.line(canvas, (xp, yp),
                         (x1, y1),
                         draw_color, thickness)

                xp, yp = x1, y1

            mp_draw.draw_landmarks(img, handLms,
                                   mp_hands.HAND_CONNECTIONS)

    # ================= Merge Canvas =================
    img_gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
    _, img_inv = cv2.threshold(img_gray, 50, 255,
                               cv2.THRESH_BINARY_INV)
    img_inv = cv2.cvtColor(img_inv, cv2.COLOR_GRAY2BGR)

    img = cv2.bitwise_and(img, img_inv)
    img = cv2.bitwise_or(img, canvas)
   

    cv2.imshow("Virtual Finger Drawing", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
