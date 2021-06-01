# dependencies
import os, sys, cv2, pytesseract

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # adds project dir to places it looks for the modules
sys.path.append(BASE_PATH)

if __name__ == '__main__':
    from config import pytesseract_location
else:
    from lib.config import pytesseract_location

# tell pytesseract where to look
pytesseract.pytesseract.tesseract_cmd = pytesseract_location

class Processor():
    def __init__(self, image_path):
        self.original_image = cv2.imread(image_path)
        self.black_and_white_img = ''
        self.text_from_img = ''
    
    def turn_black_and_white(self):
        gray_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
        (thresh, self.black_and_white_img) = cv2.threshold(gray_image, 172, 255, cv2.THRESH_BINARY)
    
    def image_to_txt(self):
        self.text_from_img = pytesseract.image_to_string(self.black_and_white_img).strip().lower().replace('\n',' ')


if __name__ == "__main__":
    processor = Processor('.data/images/test/real1.png')
    processor.turn_black_and_white()
    processor.image_to_txt()

    print(processor.text_from_img)