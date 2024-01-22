import cv2
import pytesseract
from pytesseract import Output
import numpy as np
from boxdetect import config
from boxdetect.pipelines import get_checkboxes
# from utils import warpper

def segmentation(original_image,x,y,weidth,height):
    cv2.rectangle(original_image,(x,y),(x+weidth,y+height),(0,255,0),2)
    cv2.putText(original_image,'Middle_section',(x+2,y+10),0,0.3,(0,255,0))
    return original_image[y:y+height,x:x+weidth]



def process_part(img):
    img_copy = img.copy() 
    d = pytesseract.image_to_data(img, config='--psm 6', output_type=Output.DICT)
    print(d["text"])
    cfg = config.PipelinesConfig()
    cfg.width_range = (25, 50)
    cfg.height_range = (25, 50)
    cfg.scaling_factors = [0.7]
    cfg.wh_ratio_range = (0.8, 1.2)
    checkboxes = get_checkboxes(img, cfg=cfg, px_threshold=0.5, plot=False, verbose=True)

    checkbox_texts = []
    for checkbox in checkboxes:
        x, y, w, h = checkbox[0]
        color = (0, 255, 0)
        cv2.rectangle(img_copy, (x, y), (x+w, y+h), color, 2)
        associated_texts = []
        center_y = y + h / 2  # calculate the vertical center of the checkbox

        for i in range(len(d['text'])):
            # Calculate the text's bottom (top + height) and center (average of top and bottom)
            text_top = int(d['top'][i])
            text_height = int(d['height'][i])
            text_bottom = text_top + text_height
            text_center = (text_top + text_bottom) / 2

            # Find all the text on the right side of the checkbox within 200 pixels distance
            # Compare the vertical position of the text center to the center of the checkbox
            if x < int(d['left'][i]) < x + w + 1000 and abs(center_y - text_center) <= 30:
                associated_texts.append(d['text'][i])
        
        checkbox_texts.append(associated_texts)
        color = (0, 255, 0)
        cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)

    res = []
    for checkbox, text in zip(checkboxes, checkbox_texts):
        # print(f'Checkbox at {checkbox[0]}, unchecked text: {" ".join(text)}')
        res.append(" ".join(text))

    return res, img_copy
def process_part_50(img):
    img_copy = img.copy() 
    d = pytesseract.image_to_data(img, config='--psm 6', output_type=Output.DICT)
    
    cfg = config.PipelinesConfig()
    cfg.width_range = (25, 50)
    cfg.height_range = (23, 50)
    cfg.scaling_factors = [0.9]
    cfg.wh_ratio_range = (0.6, 1.2)
    checkboxes = get_checkboxes(img, cfg=cfg, px_threshold=0.5, plot=False, verbose=True)

    checkbox_texts = []
    for checkbox in checkboxes:
        x, y, w, h = checkbox[0]
        color = (0, 255, 0)
        cv2.rectangle(img_copy, (x, y), (x+w, y+h), color, 2)
        associated_texts = []
        center_y = y + h / 2  # calculate the vertical center of the checkbox

        for i in range(len(d['text'])):
            # Calculate the text's bottom (top + height) and center (average of top and bottom)
            text_top = int(d['top'][i])
            text_height = int(d['height'][i])
            text_bottom = text_top + text_height
            text_center = (text_top + text_bottom) / 2

            # Find all the text on the right side of the checkbox within 200 pixels distance
            # Compare the vertical position of the text center to the center of the checkbox
            if x < int(d['left'][i]) < x + w + 1000 and abs(center_y - text_center) <= 30:
                associated_texts.append(d['text'][i])
        
        checkbox_texts.append(associated_texts)
        color = (0, 255, 0)
        cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)

    res = []
    for checkbox, text in zip(checkboxes, checkbox_texts):
        # print(f'Checkbox at {checkbox[0]}, unchecked text: {" ".join(text)}')
        res.append(" ".join(text))

    return res, img_copy
def process_part_11(img):
    img_copy = img.copy() 
    d = pytesseract.image_to_data(img, config='--psm 6', output_type=Output.DICT)
    # print(d)
    cfg = config.PipelinesConfig()
    cfg.width_range = (28, 50)
    cfg.height_range = (25, 50)
    cfg.scaling_factors = [0.7]
    cfg.wh_ratio_range = (0.7, 1.2)
    checkboxes = get_checkboxes(img, cfg=cfg, px_threshold=0.5, plot=False, verbose=True)

    checkbox_texts = []
    for checkbox in checkboxes:
        x, y, w, h = checkbox[0]
        color = (0, 255, 0)
        cv2.rectangle(img_copy, (x, y), (x+w, y+h), color, 2)
        associated_texts = []
        center_y = y + h / 2  # calculate the vertical center of the checkbox

        for i in range(len(d['text'])):
            # Calculate the text's bottom (top + height) and center (average of top and bottom)
            text_top = int(d['top'][i])
            text_height = int(d['height'][i])
            text_bottom = text_top + text_height
            text_center = (text_top + text_bottom) / 2

            # Find all the text on the right side of the checkbox within 200 pixels distance
            # Compare the vertical position of the text center to the center of the checkbox
            if x < int(d['left'][i]) < x + w + 1000 and (-25 < (text_center - center_y) < 100):
                associated_texts.append(d['text'][i])
        
        checkbox_texts.append(associated_texts)
        color = (0, 255, 0)
        cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)

    res = []
    for checkbox, text in zip(checkboxes, checkbox_texts):
        # print(f'Checkbox at {checkbox[0]}, unchecked text: {" ".join(text)}')
        res.append(" ".join(text))

    return res, img_copy
def process_part_11_50(img):
    img_copy = img.copy() 
    d = pytesseract.image_to_data(img, config='--psm 6', output_type=Output.DICT)
    # print(d)
    cfg = config.PipelinesConfig()
    cfg.width_range = (25, 50)
    cfg.height_range = (23, 50)
    cfg.scaling_factors = [0.9]
    cfg.wh_ratio_range = (0.8, 1.2)
    checkboxes = get_checkboxes(img, cfg=cfg, px_threshold=0.5, plot=False, verbose=True)

    checkbox_texts = []
    for checkbox in checkboxes:
        x, y, w, h = checkbox[0]
        color = (0, 255, 0)
        cv2.rectangle(img_copy, (x, y), (x+w, y+h), color, 2)
        associated_texts = []
        center_y = y + h / 2  # calculate the vertical center of the checkbox

        for i in range(len(d['text'])):
            # Calculate the text's bottom (top + height) and center (average of top and bottom)
            text_top = int(d['top'][i])
            text_height = int(d['height'][i])
            text_bottom = text_top + text_height
            text_center = (text_top + text_bottom) / 2

            # Find all the text on the right side of the checkbox within 200 pixels distance
            # Compare the vertical position of the text center to the center of the checkbox
            if x < int(d['left'][i]) < x + w + 1000 and (-25 < (text_center - center_y) < 100):
                associated_texts.append(d['text'][i])
        
        checkbox_texts.append(associated_texts)
        color = (0, 255, 0)
        cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)

    res = []
    for checkbox, text in zip(checkboxes, checkbox_texts):
        # print(f'Checkbox at {checkbox[0]}, unchecked text: {" ".join(text)}')
        res.append(" ".join(text))

    return res, img_copy

def process_part_short(img):
    img_copy = img.copy() 
    d = pytesseract.image_to_data(img, config='--psm 6', output_type=Output.DICT)
    print(d["text"])
    cfg = config.PipelinesConfig()
    cfg.width_range = (28, 50)
    cfg.height_range = (25, 50)
    cfg.scaling_factors = [0.8]
    cfg.wh_ratio_range = (0.8, 1.2)
    checkboxes = get_checkboxes(img, cfg=cfg, px_threshold=0.5, plot=False, verbose=True)

    checkbox_texts = []
    for checkbox in checkboxes:
        x, y, w, h = checkbox[0]
        color = (0, 255, 0)
        cv2.rectangle(img_copy, (x, y), (x+w, y+h), color, 2)
        associated_texts = []
        center_y = y + h / 2  # calculate the vertical center of the checkbox

        for i in range(len(d['text'])):
            # Calculate the text's bottom (top + height) and center (average of top and bottom)
            text_top = int(d['top'][i])
            text_height = int(d['height'][i])
            text_bottom = text_top + text_height
            text_center = (text_top + text_bottom) / 2

            # Find all the text on the right side of the checkbox within 200 pixels distance
            # Compare the vertical position of the text center to the center of the checkbox
            if x < int(d['left'][i]) < x + w + 350 and abs(center_y - text_center) <= 30:
                associated_texts.append(d['text'][i])
        
        checkbox_texts.append(associated_texts)
        color = (0, 255, 0)
        cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)

    res = []
    for checkbox, text in zip(checkboxes, checkbox_texts):
        # print(f'Checkbox at {checkbox[0]}, unchecked text: {" ".join(text)}')
        res.append(" ".join(text))

    return res, img_copy
def process_part_short_50(img):
    img_copy = img.copy() 
    d = pytesseract.image_to_data(img, config='--psm 6', output_type=Output.DICT)
    cfg = config.PipelinesConfig()
    cfg.width_range = (25, 50)
    cfg.height_range = (23, 50)
    cfg.scaling_factors = [0.7]
    cfg.wh_ratio_range = (0.6, 1.2)
    checkboxes = get_checkboxes(img, cfg=cfg, px_threshold=0.5, plot=False, verbose=True)

    checkbox_texts = []
    for checkbox in checkboxes:
        x, y, w, h = checkbox[0]
        color = (0, 255, 0)
        cv2.rectangle(img_copy, (x, y), (x+w, y+h), color, 2)
        associated_texts = []
        center_y = y + h / 2  # calculate the vertical center of the checkbox

        for i in range(len(d['text'])):
            # Calculate the text's bottom (top + height) and center (average of top and bottom)
            text_top = int(d['top'][i])
            text_height = int(d['height'][i])
            text_bottom = text_top + text_height
            text_center = (text_top + text_bottom) / 2

            # Find all the text on the right side of the checkbox within 200 pixels distance
            # Compare the vertical position of the text center to the center of the checkbox
            if x < int(d['left'][i]) < x + w + 350 and abs(center_y - text_center) <= 30:
                associated_texts.append(d['text'][i])
        
        checkbox_texts.append(associated_texts)
        color = (0, 255, 0)
        cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)

    res = []
    for checkbox, text in zip(checkboxes, checkbox_texts):
        # print(f'Checkbox at {checkbox[0]}, unchecked text: {" ".join(text)}')
        res.append(" ".join(text))

    return res, img_copy

def get_detected_sentences(file_path, output_path):
    img = cv2.imread(file_path)
    osd = pytesseract.image_to_osd(img, output_type=Output.DICT)
    rotate_angle = osd['rotate']
    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, rotate_angle, 1.0)
    img = cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
    # min_x, min_y, max_x, max_y = warpper.detector(img)

    # base_y = max_y + 100

    Q9_boundaries = (100, 800, 1450, 1050)  # x, y, width, height
    Q10_boundaries = (100, 1850, 1450, 1050) 
    Q11_boundaries = (1700, 180, 1450, 1500) 
    Q12_boundaries = (1700, 1700, 1450, 1220) 
    Q13_boundaries = (3150, 200, 1450, 850)
    Q14_boundaries = (3150, 1050, 1450, 700) 
    Q15_boundaries = (3150, 1800, 1450, 550)
    Q16_boundaries = (3150, 2350, 1450, 660)
    Q17_boundaries = (3150, 3010, 1450, 750)

    Q9 = segmentation(img, *Q9_boundaries)
    Q10 = segmentation(img, *Q10_boundaries)
    Q11 = segmentation(img, *Q11_boundaries)
    Q12 = segmentation(img, *Q12_boundaries)
    Q13 = segmentation(img, *Q13_boundaries)
    Q14 = segmentation(img, *Q14_boundaries)
    Q15 = segmentation(img, *Q15_boundaries)
    Q16 = segmentation(img, *Q16_boundaries)
    Q17 = segmentation(img, *Q17_boundaries)
    Q9_res, Q9_marked = process_part(Q9)
    Q10_res, Q10_marked = process_part(Q10)
    Q11_res, Q11_marked = process_part_11(Q11)
    Q12_res, Q12_marked = process_part(Q12)
    Q13_res, Q13_marked = process_part(Q13)
    Q14_res, Q14_marked = process_part(Q14)
    Q15_res, Q15_marked = process_part_short(Q15)
    Q16_res, Q16_marked = process_part(Q16)
    Q17_res, Q17_marked = process_part_short(Q17)
    marked_image = np.vstack((Q9_marked, Q10_marked, Q11_marked, Q12_marked, Q13_marked, Q14_marked, Q15_marked, Q16_marked, Q17_marked))
    cv2.imwrite(output_path, marked_image)

    return Q9_res, Q10_res, Q11_res, Q12_res, Q13_res, Q14_res, Q15_res, Q16_res, Q17_res

def get_detected_sentences_50(file_path, output_path):
    img = cv2.imread(file_path)
    osd = pytesseract.image_to_osd(img, output_type=Output.DICT)
    rotate_angle = osd['rotate']
    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, rotate_angle, 1.0)
    img = cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
    # min_x, min_y, max_x, max_y = warpper.detector(img)

    # base_y = max_y + 100

    Q9_boundaries = (100, 900, 1450, 1050)  # x, y, width, height
    Q10_boundaries = (100, 2000, 1450, 1050) 
    Q11_boundaries = (1700, 180, 1450, 1500) 
    Q12_boundaries = (1700, 1700, 1450, 1220) 
    Q13_boundaries = (3150, 200, 1450, 850)
    Q14_boundaries = (3150, 1050, 1450, 700) 
    Q15_boundaries = (3150, 1750, 1450, 550)
    Q16_boundaries = (3150, 2350, 1450, 660)
    Q17_boundaries = (3150, 3010, 1450, 750)

    Q9 = segmentation(img, *Q9_boundaries)
    Q10 = segmentation(img, *Q10_boundaries)
    Q11 = segmentation(img, *Q11_boundaries)
    Q12 = segmentation(img, *Q12_boundaries)
    Q13 = segmentation(img, *Q13_boundaries)
    Q14 = segmentation(img, *Q14_boundaries)
    Q15 = segmentation(img, *Q15_boundaries)
    Q16 = segmentation(img, *Q16_boundaries)
    Q17 = segmentation(img, *Q17_boundaries)
    Q9_res, Q9_marked = process_part_50(Q9)
    Q10_res, Q10_marked = process_part_50(Q10)
    Q11_res, Q11_marked = process_part_11_50(Q11)
    Q12_res, Q12_marked = process_part_50(Q12)
    Q13_res, Q13_marked = process_part_50(Q13)
    Q14_res, Q14_marked = process_part_50(Q14)
    Q15_res, Q15_marked = process_part_short_50(Q15)
    Q16_res, Q16_marked = process_part_50(Q16)
    Q17_res, Q17_marked = process_part_short_50(Q17)
    marked_image = np.vstack((Q9_marked, Q10_marked, Q11_marked, Q12_marked, Q13_marked, Q14_marked, Q15_marked, Q16_marked, Q17_marked))
    cv2.imwrite(output_path, marked_image)

    return Q9_res, Q10_res, Q11_res, Q12_res, Q13_res, Q14_res, Q15_res, Q16_res, Q17_res


