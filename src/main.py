import cv2
from easytello import tello
import time


def main(self):
    # Creating stream capture object
    cap = cv2.VideoCapture('udp://@192.168.10.1:11111')

    # Runs while 'stream_state' is True
    while True:
        ret, last_frame = cap.read()
        cv2.imshow('DJI Tello', last_frame)

        # Video Stream is closed if escape key is pressed
        k = cv2.waitKey(1) & 0xFF

        # Control loop
        if k == 87 or k == 38:  # w or up
            self.forward(0.1)
        elif k == 65 or k == 37:  # a or left
            self.left(0.1)
        elif k == 83 or k == 40:  # s or down
            self.back(0.1)
        elif k == 68 or k == 39:  # d or right
            self.right(0.1)
        elif k == 27:  # esc
            self.land()
            break

    cap.release()
    cv2.destroyAllWindows()


drone = tello.Tello()
setattr(drone, 'main', main) 

drone.send_command('streamon')
drone.video()
