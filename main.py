# dependencies
import os, sys, time, datetime, cv2, pytesseract
from fuzzywuzzy import fuzz

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # adds project dir to places it looks for the modules
sys.path.append(BASE_PATH)

from test.main_test import _App
from lib.screenshot import Camera, on_click
from lib.proccess_img import Processor
from lib.proccess_text import Text_Processor
from lib.loud import Speaker
from lib.key_press import Controler
from lib.config import pytesseract_location

pytesseract.pytesseract.tesseract_cmd = pytesseract_location

running = True
print('type "help" for help')
while running:
    user_input = input('$').strip().lower()
    if user_input == 'kill':
        running = False
    elif user_input == 'test':
        # run tester
        tester = _App()
        tester.run_all_tests()
    elif user_input == 'help':
        print('"kill" - kill the program')
        print('"test" - run all unit and integration test')
        print('"start" - starts the loop to search for pokemon')
    elif user_input == 'start':
        # set the screen shot zone
        camera = Camera(on_click)
        camera.start_mouse_listener()

        # loop
        flag = True
        while flag:

            # take screen shot
            camera.take_screenshot()

            # get text
            processor = Processor('.data/images/screenshot.png')
            processor.turn_black_and_white()
            processor.image_to_txt()

            text = processor.text_from_img

            # check text
            text_processor = Text_Processor(text)
            text_processor.proccess_text()

            # alert and save the ss if found
            if text_processor.pokemon_spawned:
                '''# get the the ss
                ss = processor.original_image
                # generate file name
                base_path = '.data/images/successes/'
                file_name = str(datetime.datetime.now())
                file_name = file_name.replace('-','_').replace('.',':').replace(':','-') + '.png'
                # save the image
                cv2.imwrite(base_path + file_name, ss)'''

                # type lt and see if the red text can be found on the screen
                controler = Controler()
                controler.type_lt()

                # screen shot
                camera.take_screenshot()

                # convert to gray
                img = cv2.imread('.data/images/screenshot.png')
                gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                (thresh, gray_image) = cv2.threshold(gray_image, 130, 255, cv2.THRESH_BINARY)

                # convert to string
                text = pytesseract.image_to_string(gray_image).strip().lower().replace('\n',' ')
                
                text_list = text.split(' ')

                # compare to lt when no leggy
                no_leggy = 'no legendary pokémon is spawned on you'
                for x in range(0,len(text_list)):
                    spliced_text = ''
                    start_i = x
                    end_i = x + 7 if x + 7 < len(text_list) else len(text_list)
                    for x in range(start_i,end_i):
                        spliced_text += text_list[x] + ' '
                    confidence = fuzz.ratio(spliced_text,no_leggy)

                    located = True if confidence >= 90 else False
                    if located:
                        break

                cv2.imwrite('.data/images/del.png', gray_image)
                
                # if the red text was not located alert the user
                if not located:
                    # alert the user
                    speaker = Speaker(3)
                    speaker.play()

            # wait 
            time.sleep(2)

