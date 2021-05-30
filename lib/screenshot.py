# dependencies
import os, sys, time, pyautogui

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # adds project dir to places it looks for the modules
sys.path.append(BASE_PATH)

# for later region=(left,top, width, height)

#pyautogui.displayMousePosition()
#x, y = pyautogui.position()

class Camera():
    def __init__ (self):
        x1, y1 = pyautogui.position()
        self.left = x1
        self.top = y1

        self.width = 0
        self.height = 0
 

#if __name__ == "__main__":
#    camera = Camera()

