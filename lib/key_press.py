import pyautogui, time

class Controler():
    def __init__(self):
        self.ping = 200
    def type_lt(self):
        # press '/'
        pyautogui.keyDown('/')
        time.sleep(0.2)
        pyautogui.keyUp('/')

        # press 'l'
        pyautogui.keyDown('l')
        time.sleep(0.2)
        pyautogui.keyUp('l')

        # press 't'
        pyautogui.keyDown('t')
        time.sleep(0.2)
        pyautogui.keyUp('t')

        # press enter
        pyautogui.keyDown('enter')
        time.sleep(0.2)
        pyautogui.keyUp('enter')        

if __name__ == '__main__':
    controler = Controler()
    controler.type_lt()