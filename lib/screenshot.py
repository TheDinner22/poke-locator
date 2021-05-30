# dependencies
import os, sys, pyautogui, time
from pynput import mouse

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # adds project dir to places it looks for the modules
sys.path.append(BASE_PATH)

# for later region=(left,top, width, height)

#pyautogui.displayMousePosition()
#x, y = pyautogui.position()

# called when left mouse is clicked
def on_click(x, y, button, pressed):
    x, y = pyautogui.position()
    if button == mouse.Button.left:
        border_file_path = '.data/ss_info/borders.txt'
        with open(border_file_path,'r+') as file_object:
            lines_num = len(file_object.readlines())
            if lines_num == 1:
                line = f"x2:{x}, y2:{y}"
                file_object.write(line)

                #stop listening for the mouse
                return False
            elif lines_num == 0:
                line = f"x1:{x}, y1:{y}\n"
                file_object.write(line)         
            else:
                # reset the file
                with open(border_file_path, 'w') as file_object:
                    file_object.write('')
                # write line one
                with open(border_file_path, 'a') as file_object:
                    line = f"x1:{x}, y1:{y}\n"
                    file_object.write(line)

class Camera():
    def __init__ (self, on_click_func):
        self.left = 0
        self.top = 0
        self.width = 0
        self.height = 0
        self.listener = ''
        self.on_click_function = on_click_func
        self.border_file_path = '.data/ss_info/borders.txt'
        self.screenshot_file_path = '.data/images/screenshot.png'

    def start_mouse_listener(self):
        """note this acts like time.sleep and holds up the program"""
        # listen for mouse clicks
        self.listener = mouse.Listener(on_click=self.on_click_function)
        self.listener.start()
        self.listener.join()

        # get x1, x2, y1, y2
        with open(self.border_file_path, 'r') as file_object:
            lines_list = file_object.readlines()
        x1 = lines_list[0].split(',')[0].split(':')[1].strip()
        y1 = lines_list[0].split(',')[1].split(':')[1].strip()
        x2 = lines_list[1].split(',')[0].split(':')[1].strip()
        y2 = lines_list[1].split(',')[1].split(':')[1].strip()

        # assign the left, top, width, height
        self.left = int(x1)
        self.top = int(y1)
        self.width = int(x2) - int(x1)
        self.height = int(y2) - int(y1)
        

    def take_screenshot(self):
        """take a screenshot"""
        pyautogui.screenshot(self.screenshot_file_path, region=((self.left, self.top, self.width, self.height)))

if __name__ == "__main__":
    time.sleep(5)
    camera = Camera(on_click)
    camera.start_mouse_listener()
    camera.take_screenshot()
