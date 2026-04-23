import cv2
import numpy as np
from PIL import Image

def crop_black_borders(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    _, thresh = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        c = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        cropped_image = image[y:y+h, x:x+w]
        return cropped_image
    return image

def process_eye_image(image_pil):
    image_np = np.array(image_pil.convert('RGB')) 
    image_cropped = crop_black_borders(image_np)
    image_resized = cv2.resize(image_cropped, (224, 224))
    lab = cv2.cvtColor(image_resized, cv2.COLOR_RGB2LAB)
    l, a, b = cv2.split(lab)
    
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    cl = clahe.apply(l)
    
    limg = cv2.merge((cl, a, b))
    image_clahe = cv2.cvtColor(limg, cv2.COLOR_LAB2RGB)

    image_blur = cv2.GaussianBlur(image_clahe, (3, 3), 0)
    image_for_ui = Image.fromarray(image_blur)

    image_normalized = image_blur.astype(np.float32) / 255.0
    mean = np.array([0.485, 0.456, 0.406])
    std = np.array([0.229, 0.224, 0.225])
    
    image_ready_for_model = (image_normalized - mean) / std
    image_ready_for_model = np.transpose(image_ready_for_model, (2, 0, 1))

    return image_for_ui, image_ready_for_model