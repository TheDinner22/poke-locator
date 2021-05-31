#https://pypi.org/project/playsound/
# dependencies
import os, sys, random

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # adds project dir to places it looks for the modules
sys.path.append(BASE_PATH)

from playsound import playsound

class Speaker():
    def __init__(self):
        self.base_path = '.data/sounds/'
        self.contents = os.listdir(self.base_path)
    
    def play(self):
        '''plays a random file from the sounds dir'''
        if(len(self.contents) > 0):
            pass # check extension here

if __name__ == "__main__":
    speaker = Speaker()
    print(speaker.contents)
