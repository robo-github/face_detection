import cv2

import numpy as np

def has_face(image_path):
    
    detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') # Load the detector
    
   
    with open(image_path, 'rb') as f:
        image_data = np.fromfile(f, np.uint8)
    
    # Decode the image data to get the image
    image = cv2.imdecode(image_data, cv2.IMREAD_COLOR)
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the image
    rects = detector.detectMultiScale(gray, 1.1, 4)
    
    
    if len(rects) == 0:  # If no face is detected, return False
        return False
    
    elif len(rects) == 1:  # If exactly one face is detected, return True
        return True
   
    else:    # If more than one face is detected, return False
        return False


