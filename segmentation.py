# import cv2
# import pytesseract
# def segmentation(img,x,y,weidth,height):
#     img = img[y:y+height,x:x+weidth]
#     cv2.imshow("segmented",img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#     return img
# def extract_text(image):
#     # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # 在 Windows 中，需要指定 Tesseract-OCR 的安装路径
#     text = pytesseract.image_to_string(image)
#     return text
# if __name__ == "__main__":
    
#     image_path = r"./images/Philly/page_0.png"

#     original_image = cv2.imread(image_path)

#     # edged_image, original_resized_image, ratio= edgeDetect(image_path)
#     # contoured_image, screencnt= contours(edged_image, original_resized_image)
#     # perspectiveTransformed_image = perspectiveTransform(original_image, screencnt, ratio)

#     x = 250
#     y = 1400
#     weidth = 3500
#     height = 1000

#     # Q1 = segmentation(original_image,x,y,weidth,height)
#     cv2.rectangle(original_image,(x,y),(x+weidth,y+height),(0,255,0),2)
#     cv2.putText(original_image,'Middle_section',(x+2,y+10),0,0.3,(0,255,0))

#     x = 250
#     y= 2600
#     weidth = 3500
#     height = 180

#     # Q2 = segmentation(original_image,x,y,weidth,height)
#     cv2.rectangle(original_image,(x,y),(x+weidth,y+height),(0,255,0),2)
#     cv2.putText(original_image,'Middle_section',(x+2,y+10),0,0.3,(0,255,0))    
#     # Q1_text = extract_text(Q1)
#     # print(Q1_text)
    
#     x = 250
#     y= 2820
#     weidth = 3500
#     height = 130

#     # Q2 = segmentation(original_image,x,y,weidth,height)
#     cv2.rectangle(original_image,(x,y),(x+weidth,y+height),(0,255,0),2)
#     cv2.putText(original_image,'Middle_section',(x+2,y+10),0,0.3,(0,255,0)) 
    
#     x = 250
#     y= 3000
#     weidth = 3500
#     height = 750

#     # Q2 = segmentation(original_image,x,y,weidth,height)
#     cv2.rectangle(original_image,(x,y),(x+weidth,y+height),(0,255,0),2)
#     cv2.putText(original_image,'Middle_section',(x+2,y+10),0,0.3,(0,255,0)) 
    
#     x = 250
#     y= 3800
#     weidth = 3500
#     height = 150

#     # Q2 = segmentation(original_image,x,y,weidth,height)
#     cv2.rectangle(original_image,(x,y),(x+weidth,y+height),(0,255,0),2)
#     cv2.putText(original_image,'Middle_section',(x+2,y+10),0,0.3,(0,255,0)) 
       
#     x = 250
#     y= 3950
#     weidth = 3500
#     height = 700

#     # Q2 = segmentation(original_image,x,y,weidth,height)
#     cv2.rectangle(original_image,(x,y),(x+weidth,y+height),(0,255,0),2)
#     cv2.putText(original_image,'Middle_section',(x+2,y+10),0,0.3,(0,255,0)) 
       
#     x = 250
#     y= 4680
#     weidth = 3500
#     height = 180

#     # Q2 = segmentation(original_image,x,y,weidth,height)
#     cv2.rectangle(original_image,(x,y),(x+weidth,y+height),(0,255,0),2)
#     cv2.putText(original_image,'Middle_section',(x+2,y+10),0,0.3,(0,255,0)) 
       
#     cv2.imshow("boxed", original_image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
    
import cv2
import pytesseract
def segmentation(img,x,y,weidth,height):
    img = img[y:y+height,x:x+weidth]
    cv2.imshow("segmented",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return img
def extract_text(image):
    # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # 在 Windows 中，需要指定 Tesseract-OCR 的安装路径
    text = pytesseract.image_to_string(image)
    return text
if __name__ == "__main__":
    
    image_path = r"./images/Philly/page_1.png"

    original_image = cv2.imread(image_path)

    # edged_image, original_resized_image, ratio= edgeDetect(image_path)
    # contoured_image, screencnt= contours(edged_image, original_resized_image)
    # perspectiveTransformed_image = perspectiveTransform(original_image, screencnt, ratio)

    x = 100
    y = 800
    weidth = 1600
    height = 1050

    # Q1 = segmentation(original_image,x,y,weidth,height)
    cv2.rectangle(original_image,(x,y),(x+weidth,y+height),(0,255,0),2)
    cv2.putText(original_image,'Middle_section',(x+2,y+10),0,0.3,(0,255,0))

    x = 100
    y = 1900
    weidth = 1600
    height = 1050
    # Q2 = segmentation(original_image,x,y,weidth,height)
    cv2.rectangle(original_image,(x,y),(x+weidth,y+height),(0,255,0),2)
    cv2.putText(original_image,'Middle_section',(x+2,y+10),0,0.3,(0,255,0))    

    
    x = 1750
    y = 180
    weidth = 1450
    height = 1500

    # Q3 = segmentation(original_image,x,y,weidth,height)
    cv2.rectangle(original_image,(x,y),(x+weidth,y+height),(0,255,0),2)
    cv2.putText(original_image,'Middle_section',(x+2,y+10),0,0.3,(0,255,0)) 
    
    x = 1750
    y = 1700
    weidth = 1450
    height = 1220

    # Q4 = segmentation(original_image,x,y,weidth,height)
    cv2.rectangle(original_image,(x,y),(x+weidth,y+height),(0,255,0),2)
    cv2.putText(original_image,'Middle_section',(x+2,y+10),0,0.3,(0,255,0)) 
    
    x = 3200
    y = 200
    weidth = 1700
    height = 850
    print((x, y, weidth, height))
    # Q5 = segmentation(original_image,x,y,weidth,height)
    cv2.rectangle(original_image,(x,y),(x+weidth,y+height),(0,255,0),2)
    cv2.putText(original_image,'Middle_section',(x+2,y+10),0,0.3,(0,255,0)) 
       
    x = 3200
    y = 1050
    weidth = 1700
    height = 700
    print((x, y, weidth, height))
    # Q6 = segmentation(original_image,x,y,weidth,height)
    cv2.rectangle(original_image,(x,y),(x+weidth,y+height),(0,255,0),2)
    cv2.putText(original_image,'Middle_section',(x+2,y+10),0,0.3,(0,255,0)) 
       
    x = 3200
    y = 1750
    weidth = 1700
    height = 550
    print((x, y, weidth, height))
    # Q7 = segmentation(original_image,x,y,weidth,height)
    cv2.rectangle(original_image,(x,y),(x+weidth,y+height),(0,255,0),2)
    cv2.putText(original_image,'Middle_section',(x+2,y+10),0,0.3,(0,255,0)) 
    
    x = 3200
    y = 2350
    weidth = 1700
    height = 680
    print((x, y, weidth, height))
    # Q8 = segmentation(original_image,x,y,weidth,height)
    cv2.rectangle(original_image,(x,y),(x+weidth,y+height),(0,255,0),2)
    cv2.putText(original_image,'Middle_section',(x+2,y+10),0,0.3,(0,255,0)) 
       
    x = 3150
    y = 3030
    weidth = 1800
    height = 750
    print((x, y, weidth, height))
    # Q9 = segmentation(original_image,x,y,weidth,height)
    cv2.rectangle(original_image,(x,y),(x+weidth,y+height),(0,255,0),2)
    cv2.putText(original_image,'Middle_section',(x+2,y+10),0,0.3,(0,255,0)) 
       
    cv2.imshow("boxed", original_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    