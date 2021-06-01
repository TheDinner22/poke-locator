unit_tests = {}

# dependencies
import os, sys

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # adds project dir to places it looks for the modules
sys.path.append(BASE_PATH)

from lib.config import pytesseract_location

# make sure all of the needed libraries are installed and working
def test1(done):
    '''make sure all of the needed libraries are installed and working'''
    try:
        # import all of the libraries used in this project, if there are no errors, they are all installed
        import pyautogui, cv2, pynput, fuzzywuzzy, playsound, pytesseract

        # also make the sure file-side of pytesseract is installed
        # tell pytesseract where to look
        pytesseract.pytesseract.tesseract_cmd = pytesseract_location

        # run a function from pytesseract to make sure the pip part and the file-side work together
        image = cv2.imread('.data/images/test/fake.png')
        _string = pytesseract.image_to_string(image)

        # if none of this threw the test passes
        done('make sure all of the needed libraries are installed and working')
    except Exception as e:
        e = str(e) 
        raise AssertionError('importing/using one of the libraries from this project caused this error:\n' + e)
unit_tests['make sure all of the needed libraries are installed and working'] = test1


'''
# example tests
def one_plus_one_is_two(done):
    outcome = 1+1
    desired_outcome = 2
    assert outcome == desired_outcome, "1+1 was not equal to two"
    done("one plus one is equal to two")
unit_tests["one plus one is equal to two"] = one_plus_one_is_two

def one_plus_one_is_three(done):
    outcome = 1+1
    desired_outcome = 3
    assert outcome == desired_outcome, "1+1 was not equal to three"
    done("one plus one is equal to three")
unit_tests["one plus one is equal to three"] = one_plus_one_is_three
'''
