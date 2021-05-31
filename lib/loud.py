#https://pypi.org/project/playsound/
# dependencies
import os, sys, random

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # adds project dir to places it looks for the modules
sys.path.append(BASE_PATH)

from playsound import playsound

class Speaker():
    def __init__(self, number_of_plays):
        self.base_path = '.data/sounds/'
        self.contents = os.listdir(self.base_path)
        self.number_of_plays = number_of_plays if number_of_plays > 0 else 1 
    
    def play(self):
        '''plays a random file from the sounds dir'''
        if(len(self.contents) > 0):
            flag = True
            while flag:
                # get the file name
                number = random.randint(0,len(self.contents)-1)
                file_name = self.contents[number]
                # make sure its mp3
                if file_name.find('.') != -1:
                    extension = file_name.split('.').pop().lower()
                    if extension == 'mp3':
                        flag = False
                        break
            # just play the file 3 times
            full_path = self.base_path + file_name
            for _x in range(0,self.number_of_plays):
                playsound(full_path)

if __name__ == "__main__":
    speaker = Speaker()
    speaker.play()
