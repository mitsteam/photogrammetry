import cv2
from easytello import tello
import time

def input_stuff() -> list:
    print("Please input the dimensions of your object in cm below.")

    width = int(input("Width: "))
    height = int(input("Height: "))

    return [width, height]
 

def video(self):
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

drone = tello.Tello()
setattr(drone, 'video', video)


drone.send_command('streamon')
drone.video()

