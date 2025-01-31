import cv2
import mediapipe as mp
import pyautogui

mp_hands = mp.solutions.hands.Hands()
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    results = mp_hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    if results.multi_hand_landmarks:
        for hand in results.multi_hand_landmarks:
            thumb_tip = hand.landmark[4]
            index_tip = hand.landmark[8]
            distance = ((thumb_tip.x - index_tip.x) ** 2 + (thumb_tip.y - index_tip.y) ** 2) ** 0.5

            volume = int(distance * 100)
            pyautogui.press("volumeup" if volume > 50 else "volumedown")

    cv2.imshow("Hand Volume Control", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
