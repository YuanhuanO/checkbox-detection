import cv2
import pytesseract
from pytesseract import Output

def detector(img):
    d = pytesseract.image_to_data(img, output_type=Output.DICT)
    n_boxes = len(d['text'])

    target_text = 'Basic'


    min_x, min_y, max_x, max_y = float('inf'), float('inf'), 0, 0


    for i in range(n_boxes):
        if d['text'][i] == target_text:

            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x + w)
            max_y = max(max_y, y + h)

    position = (min_x, min_y, max_x, max_y)
    return position


