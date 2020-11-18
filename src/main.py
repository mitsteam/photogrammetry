import cv2
from easytello import tello
import time

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

def video():
    # Creating stream capture object
    cap = cv2.VideoCapture('udp://@192.168.10.1:11111')
    # Runs while 'stream_state' is True
    while True:
        ret, last_frame = cap.read()
        cv2.imshow('DJI Tello', last_frame)

        # Video Stream is closed if escape key is pressed
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


def main():
    while True:
        k = cv2.waitKey(1)
        if k == 87: # w
            tello.left(0.1)
        elif k == 65: # a
            tello.left(0.1)
        elif k == 83: # s
            tello.left(0.1)
        elif k == 68: # d
            tello.left(0.1)
        elif k == 27: # esc
            tello.land()
            break
        
if __name__ == "__main__":
    drone = tello.Tello()
    # drone.send_command('streamon')
    # video
    main()