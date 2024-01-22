import cv2
import pytesseract
from pytesseract import Output
import numpy as np
from boxdetect import config
from boxdetect.pipelines import get_checkboxes
from utils import warpper

def segmentation(original_image,x,y,weidth,height):
    cv2.rectangle(original_image,(x,y),(x+weidth,y+height),(0,255,0),2)
    cv2.putText(original_image,'Middle_section',(x+2,y+10),0,0.3,(0,255,0))
    return original_image[y:y+height,x:x+weidth]

def process_part(img):
    img_copy = img.copy() 
    d = pytesseract.image_to_data(img, config='--psm 6', output_type=Output.DICT)

    cfg = config.PipelinesConfig()
    cfg.width_range = (30, 50)
    cfg.height_range = (30, 50)
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
            if x - w < int(d['left'][i]) < x + w + 800 and abs(center_y - text_center) <= 50:
                associated_texts.append(d['text'][i])
        
        checkbox_texts.append(associated_texts)
        color = (0, 255, 0)
        cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)

    res = []
    for checkbox, text in zip(checkboxes, checkbox_texts):
        # print(f'Checkbox at {checkbox[0]}, unchecked text: {" ".join(text)}')
        res.append(" ".join(text))

    return res, img_copy
def process_part_3(img):
    img_copy = img.copy() 
    # Use pytesseract's OSD (Orientation and Script Detection) feature to estimate the text orientation
    # osd = pytesseract.image_to_osd(img, output_type=Output.DICT)
    # rotate_angle = osd['rotate']

    # # Rotate the image to correct the skew
    # (h, w) = img.shape[:2]
    # center = (w // 2, h // 2)
    # M = cv2.getRotationMatrix2D(center, rotate_angle, 1.0)
    # img = cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)

    d = pytesseract.image_to_data(img, config='--psm 6', output_type=Output.DICT)

    cfg = config.PipelinesConfig()
    cfg.width_range = (33, 48)
    cfg.height_range = (33, 48)
    cfg.scaling_factors = [0.85]
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
            if x - 20 < int(d['left'][i]) < x + w + 400 and abs(center_y - text_center) <= 50:
                associated_texts.append(d['text'][i])
        
        checkbox_texts.append(associated_texts)
        color = (0, 255, 0)
        cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)

    res = []
    for checkbox, text in zip(checkboxes, checkbox_texts):
        # print(f'Checkbox at {checkbox[0]}, unchecked text: {" ".join(text)}')
        res.append(" ".join(text))

    return res, img_copy
def process_part_4(img):
    img_copy = img.copy() 
    # Use pytesseract's OSD (Orientation and Script Detection) feature to estimate the text orientation
    # osd = pytesseract.image_to_osd(img, output_type=Output.DICT)
    # rotate_angle = osd['rotate']

    # # Rotate the image to correct the skew
    # (h, w) = img.shape[:2]
    # center = (w // 2, h // 2)
    # M = cv2.getRotationMatrix2D(center, rotate_angle, 1.0)
    # img = cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)

    d = pytesseract.image_to_data(img, config='--psm 6', output_type=Output.DICT)

    cfg = config.PipelinesConfig()
    cfg.width_range = (33, 48)
    cfg.height_range = (33, 48)
    cfg.scaling_factors = [0.85]
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
            if x - 40 < int(d['left'][i]) < x + w + 200 and abs(center_y - text_center) <= 50:
                associated_texts.append(d['text'][i])
        
        checkbox_texts.append(associated_texts)
        color = (0, 255, 0)
        cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)

    res = []
    for checkbox, text in zip(checkboxes, checkbox_texts):
        # print(f'Checkbox at {checkbox[0]}, unchecked text: {" ".join(text)}')
        res.append(" ".join(text))

    return res, img_copy
def process_part_6(img):
    img_copy = img.copy() 
    # Use pytesseract's OSD (Orientation and Script Detection) feature to estimate the text orientation
    # osd = pytesseract.image_to_osd(img, output_type=Output.DICT)
    # rotate_angle = osd['rotate']

    # # Rotate the image to correct the skew
    # (h, w) = img.shape[:2]
    # center = (w // 2, h // 2)
    # M = cv2.getRotationMatrix2D(center, rotate_angle, 1.0)
    # img = cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)

    d = pytesseract.image_to_data(img, config='--psm 6', output_type=Output.DICT)

    cfg = config.PipelinesConfig()
    cfg.width_range = (33, 48)
    cfg.height_range = (33, 48)
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
            if x - 30 < int(d['left'][i]) < x + w + 800 and abs(center_y - text_center) <= 50:
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
    cfg.width_range = (30, 50)
    cfg.height_range = (30, 50)
    cfg.scaling_factors = [1]
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
            if x - w < int(d['left'][i]) < x + w + 800 and abs(center_y - text_center) <= 50:
                associated_texts.append(d['text'][i])
        
        checkbox_texts.append(associated_texts)
        color = (0, 255, 0)
        cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)

    res = []
    for checkbox, text in zip(checkboxes, checkbox_texts):
        # print(f'Checkbox at {checkbox[0]}, unchecked text: {" ".join(text)}')
        res.append(" ".join(text))

    return res, img_copy
def process_part_3_50(img):
    img_copy = img.copy() 
    # Use pytesseract's OSD (Orientation and Script Detection) feature to estimate the text orientation
    # osd = pytesseract.image_to_osd(img, output_type=Output.DICT)
    # rotate_angle = osd['rotate']

    # # Rotate the image to correct the skew
    # (h, w) = img.shape[:2]
    # center = (w // 2, h // 2)
    # M = cv2.getRotationMatrix2D(center, rotate_angle, 1.0)
    # img = cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)

    d = pytesseract.image_to_data(img, config='--psm 6', output_type=Output.DICT)

    cfg = config.PipelinesConfig()
    cfg.width_range = (33, 48)
    cfg.height_range = (33, 48)
    cfg.scaling_factors = [1]
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
            if x - 20 < int(d['left'][i]) < x + w + 400 and abs(center_y - text_center) <= 50:
                associated_texts.append(d['text'][i])
        
        checkbox_texts.append(associated_texts)
        color = (0, 255, 0)
        cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)

    res = []
    for checkbox, text in zip(checkboxes, checkbox_texts):
        # print(f'Checkbox at {checkbox[0]}, unchecked text: {" ".join(text)}')
        res.append(" ".join(text))

    return res, img_copy
def process_part_4_50(img):
    img_copy = img.copy() 
    # Use pytesseract's OSD (Orientation and Script Detection) feature to estimate the text orientation
    # osd = pytesseract.image_to_osd(img, output_type=Output.DICT)
    # rotate_angle = osd['rotate']

    # # Rotate the image to correct the skew
    # (h, w) = img.shape[:2]
    # center = (w // 2, h // 2)
    # M = cv2.getRotationMatrix2D(center, rotate_angle, 1.0)
    # img = cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)

    d = pytesseract.image_to_data(img, config='--psm 6', output_type=Output.DICT)

    cfg = config.PipelinesConfig()
    cfg.width_range = (33, 48)
    cfg.height_range = (33, 48)
    cfg.scaling_factors = [1]
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
            if x - 40 < int(d['left'][i]) < x + w + 200 and abs(center_y - text_center) <= 50:
                associated_texts.append(d['text'][i])
        
        checkbox_texts.append(associated_texts)
        color = (0, 255, 0)
        cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)

    res = []
    for checkbox, text in zip(checkboxes, checkbox_texts):
        # print(f'Checkbox at {checkbox[0]}, unchecked text: {" ".join(text)}')
        res.append(" ".join(text))

    return res, img_copy
def process_part_6_50(img):
    img_copy = img.copy() 
    # Use pytesseract's OSD (Orientation and Script Detection) feature to estimate the text orientation
    # osd = pytesseract.image_to_osd(img, output_type=Output.DICT)
    # rotate_angle = osd['rotate']

    # # Rotate the image to correct the skew
    # (h, w) = img.shape[:2]
    # center = (w // 2, h // 2)
    # M = cv2.getRotationMatrix2D(center, rotate_angle, 1.0)
    # img = cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)

    d = pytesseract.image_to_data(img, config='--psm 6', output_type=Output.DICT)

    cfg = config.PipelinesConfig()
    cfg.width_range = (33, 48)
    cfg.height_range = (33, 48)
    cfg.scaling_factors = [1]
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
            if x - 30 < int(d['left'][i]) < x + w + 800 and abs(center_y - text_center) <= 50:
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
    min_x, min_y, max_x, max_y = warpper.detector(img)

    base_y = max_y + 100
    # Q1_boundaries = (250, 1400, 3500, 1000)  # x, y, width, height
    # Q3_boundaries = (250, 2600, 3500, 180) 
    # Q4_boundaries = (250, 2820, 3500, 150) 
    # Q5_boundaries = (250, 3000, 3500, 750) 
    # Q6_boundaries = (250, 3800, 3500, 150) 
    # Q7_boundaries = (250, 3950, 3500, 700)  
    # Q8_boundaries = (250, 4680, 3500, 180) 
    Q1_boundaries = (250, base_y, 3500, 1050)  
    Q3_boundaries = (250, base_y + 1250, 3500, 180) 
    Q4_boundaries = (250, base_y + 1430, 3500, 200)
    Q5_boundaries = (250, base_y + 1630, 3500, 800) 
    Q6_boundaries = (250, base_y + 2430, 3500, 230)
    Q7_boundaries = (250, base_y + 2660, 3500, 800)  
    Q8_boundaries = (250, base_y + 3450, 3500, 200) 
    Q1 = segmentation(img, *Q1_boundaries)
    Q3 = segmentation(img, *Q3_boundaries)
    Q4 = segmentation(img, *Q4_boundaries)
    Q5 = segmentation(img, *Q5_boundaries)
    Q6 = segmentation(img, *Q6_boundaries)
    Q7 = segmentation(img, *Q7_boundaries)
    Q8 = segmentation(img, *Q8_boundaries)

    Q1_res, Q1_marked = process_part(Q1)
    Q3_res, Q3_marked = process_part_3(Q3)
    Q4_res, Q4_marked = process_part_4(Q4)
    Q5_res, Q5_marked = process_part(Q5)
    Q6_res, Q6_marked = process_part_6(Q6)
    Q7_res, Q7_marked = process_part(Q7)
    Q8_res, Q8_marked = process_part_4(Q8)
    marked_image = np.vstack((Q1_marked, Q3_marked, Q4_marked, Q5_marked, Q6_marked, Q7_marked, Q8_marked))
    cv2.imwrite(output_path, marked_image)

    return Q1_res, Q3_res, Q4_res, Q5_res, Q6_res, Q7_res, Q8_res
def get_detected_sentences_after_50(file_path, output_path):
    img = cv2.imread(file_path)
    osd = pytesseract.image_to_osd(img, output_type=Output.DICT)
    rotate_angle = osd['rotate']
    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, rotate_angle, 1.0)
    img = cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
    min_x, min_y, max_x, max_y = warpper.detector(img)

    base_y = max_y + 100
    # Q1_boundaries = (250, 1400, 3500, 1000)  # x, y, width, height
    # Q3_boundaries = (250, 2600, 3500, 180) 
    # Q4_boundaries = (250, 2820, 3500, 150) 
    # Q5_boundaries = (250, 3000, 3500, 750) 
    # Q6_boundaries = (250, 3800, 3500, 150) 
    # Q7_boundaries = (250, 3950, 3500, 700)  
    # Q8_boundaries = (250, 4680, 3500, 180) 
    Q1_boundaries = (250, base_y, 3500, 1000)  
    Q3_boundaries = (250, base_y + 1100, 3500, 150) 
    Q4_boundaries = (250, base_y + 1250, 3500, 170)
    Q5_boundaries = (250, base_y + 1450, 3500, 750) 
    Q6_boundaries = (250, base_y + 2200, 3500, 150)
    Q7_boundaries = (250, base_y + 2350, 3500, 700)  
    Q8_boundaries = (250, base_y + 3050, 3500, 180) 
    Q1 = segmentation(img, *Q1_boundaries)
    Q3 = segmentation(img, *Q3_boundaries)
    Q4 = segmentation(img, *Q4_boundaries)
    Q5 = segmentation(img, *Q5_boundaries)
    Q6 = segmentation(img, *Q6_boundaries)
    Q7 = segmentation(img, *Q7_boundaries)
    Q8 = segmentation(img, *Q8_boundaries)

    Q1_res, Q1_marked = process_part_50(Q1)
    Q3_res, Q3_marked = process_part_3_50(Q3)
    Q4_res, Q4_marked = process_part_4_50(Q4)
    Q5_res, Q5_marked = process_part_50(Q5)
    Q6_res, Q6_marked = process_part_6_50(Q6)
    Q7_res, Q7_marked = process_part_50(Q7)
    Q8_res, Q8_marked = process_part_4_50(Q8)
    marked_image = np.vstack((Q1_marked, Q3_marked, Q4_marked, Q5_marked, Q6_marked, Q7_marked, Q8_marked))
    cv2.imwrite(output_path, marked_image)

    return Q1_res, Q3_res, Q4_res, Q5_res, Q6_res, Q7_res, Q8_res
