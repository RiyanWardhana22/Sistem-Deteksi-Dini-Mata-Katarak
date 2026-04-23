import torch
import torch.nn as nn
from torchvision import models
import numpy as np

from pytorch_grad_cam import GradCAM
from pytorch_grad_cam.utils.image import show_cam_on_image

def get_model(num_classes=4):
    model = models.efficientnet_b3(weights=None)
    num_ftrs = model.classifier[1].in_features
    model.classifier[1] = nn.Linear(num_ftrs, num_classes)
    return model

def load_model(model_path):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = get_model(num_classes=4)
    try:
        state_dict = torch.load(model_path, map_location=device, weights_only=True)
        model.load_state_dict(state_dict)
        model.to(device)
        model.eval() 
        return model, device
    except Exception as e:
        print(f"Error loading model: {e}")
        return None, device

def predict(model, image_tensor, device):
    tensor = torch.tensor(image_tensor, dtype=torch.float32).unsqueeze(0).to(device)
    with torch.no_grad():
        outputs = model(tensor)
        probabilities = torch.nn.functional.softmax(outputs[0], dim=0)
        
    classes = ["Katarak", "Diabetic Retinopathy", "Glaukoma", "Normal"]
    result = {classes[i]: float(probabilities[i]) * 100 for i in range(len(classes))}
    result = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
    
    return result

def generate_gradcam(model, image_tensor, image_for_ui, device):
    target_layers = [model.features[-1]]
    cam = GradCAM(model=model, target_layers=target_layers)
    input_tensor = torch.tensor(image_tensor, dtype=torch.float32).unsqueeze(0).to(device)
    
    grayscale_cam = cam(input_tensor=input_tensor, targets=None)
    grayscale_cam = grayscale_cam[0, :]
    
    img_np = np.array(image_for_ui).astype(np.float32) / 255.0
    visualization = show_cam_on_image(img_np, grayscale_cam, use_rgb=True)
    
    return visualization