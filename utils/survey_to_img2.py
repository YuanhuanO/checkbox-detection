from PIL import Image
import pytesseract
from pdf2image import convert_from_path
import csv
import os
import cv2
import numpy as np


#Transfer pdf into images
pages = convert_from_path('atlanta_assess.pdf', 500)  
directory = '/Users/olivia/Desktop/smart-digitization/images/Atlanta'
#Parse multiple images
for i, image in enumerate(pages):
    image.save(os.path.join(directory, f'page_{i}.png'), 'PNG')

for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    
    if os.path.isfile(file_path) and file_path.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
        img = Image.open(file_path)
