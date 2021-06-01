# dependencies
import os, sys, time, datetime, cv2

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # adds project dir to places it looks for the modules
sys.path.append(BASE_PATH)

from test.main_test import _App
from lib.screenshot import Camera, on_click
from lib.proccess_img import Processor
from lib.proccess_text import Text_Processor
from lib.loud import Speaker

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

            print(text_processor.pokemon_spawned) #TODO del me

            # alert and save the ss if found
            if text_processor.pokemon_spawned:
                # get the the ss
                ss = processor.original_image
                # generate file name
                base_path = '.data/images/successes/'
                file_name = str(datetime.datetime.now())
                file_name = file_name.replace('-','_').replace('.',':').replace(':','-') + '.png'
                # save the image
                cv2.imwrite(base_path + file_name, ss)

                # alert the user
                speaker = Speaker(3)
                speaker.play()

            # wait 
            time.sleep(2)

