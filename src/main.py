import cv2
import easytello

# mac camera cv2 test
def mac_camera():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        cv2.imshow('haha', frame)
        cv2.imwrite('lol.png', frame)

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()