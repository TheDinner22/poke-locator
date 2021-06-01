integration_tests = {}

# dependencies
import os, sys

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # adds project dir to places it looks for the modules
sys.path.append(BASE_PATH)

from lib.proccess_img import Processor
from lib.proccess_text import Text_Processor

# get text from test images that SHOULD return true and see if they actually return true
def test1(done):
    '''get text from test images that SHOULD return true and see if they actually return true'''
    # get the four test files that should return true and add them to a list
    file_paths = ['.data/images/test/real.png','.data/images/test/real1.png','.data/images/test/real3.png']

    # loop through each file, checking if they return true or not (they all should)
    for file_path in file_paths:
            # get text
            processor = Processor(file_path)
            processor.turn_black_and_white()
            processor.image_to_txt()

            text = processor.text_from_img

            # check text
            text_processor = Text_Processor(text)
            text_processor.proccess_text()

            # check to see if it returned true of not
            msg = 'image: ' + file_path + ' did not return true'
            assert text_processor.pokemon_spawned, msg
    # if we exit the for loop without an error, this tests passes
    done('get text from test images that SHOULD return true and see if they actually return true')
integration_tests['get text from test images that SHOULD return true and see if they actually return true'] = test1

# get text from test images that SHOULD return false and see if they actually return false
def test2(done):
    '''get text from test images that SHOULD return false and see if they actually return false'''
    # get the four test files that should return false and add them to a list
    file_paths = ['.data/images/test/fake.png','.data/images/test/real2.png']

    # loop through each file, checking if they return false or not (they all should)
    for file_path in file_paths:
            # get text
            processor = Processor(file_path)
            processor.turn_black_and_white()
            processor.image_to_txt()

            text = processor.text_from_img

            # check text
            text_processor = Text_Processor(text)
            text_processor.proccess_text()

            # check to see if it returned false of not
            msg = 'image: ' + file_path + ' did not return false'
            assert not text_processor.pokemon_spawned, msg
    # if we exit the for loop without an error, this tests passes
    done('get text from test images that SHOULD return false and see if they actually return false')
integration_tests['get text from test images that SHOULD return false and see if they actually return false'] = test2

'''
# example test below
def one_plus_one_is_two(done):
    outcome = 1+1
    desired_outcome = 2
    assert outcome == desired_outcome, "1+1 was not equal to two"
    done("one plus one is equal to two")
integration_tests["one plus one is equal to two"] = one_plus_one_is_two
'''