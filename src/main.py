import cv2
from easytello import tello
import time

def input_stuff(self) -> list:
    print("Please input the dimensions of your object in cm below.")

    self.width = int(input("Width: "))
    self.height = int(input("Height: "))

    print("Done!")
 

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

def move_capture(self)

drone = tello.Tello()
setattr(drone, 'video', video)
setattr(drone, 'input_stuff', input_stuff) 

drone.input_stuff()
drone.send_command('streamon')
drone.video()

