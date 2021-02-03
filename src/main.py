import cv2
from easytello import tello
import time
import tkinter

class Config:
    def __init__(self):
        self.dimesions = None

        self.root = tkinter.Tk()
        tkinter.Button(self.root, text="Save", command=self.save_destroy)
        self.root.mainloop()
    
    def save_destroy(self):
        self.root.destroy()




def input_stuff():
    t

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

<<<<<<< HEAD
drone = tello.Tello()
flight_configs = Config()
drone.send_command('streamon')
video()

=======

def main():
    while True:
        k = cv2.waitKey(1)
        if k == 87 or k == 38: # w
            tello.forward(0.1)
        elif k == 65 or k == 37: # a
            tello.left(0.1)
        elif k == 83 or k == 40: # s
            tello.back(0.1)
        elif k == 68 or k == 39: # d
            tello.right(0.1)
        elif k == 27: # esc
            tello.land()
            break
        
if __name__ == "__main__":
    drone = tello.Tello()
    # drone.send_command('streamon')
    # video
    main()
>>>>>>> 2d7263c8d7035582f6e808fb745930e9b6208386
