from PIL import Image
import torch
from torchvision import models, transforms
import torch.nn as nn
from huggingface_hub import hf_hub_download

class Classification:
    def __init__(self):
        # Dictionary corresponding to shoe type (model outputs a numerical index)
        self.class_labels = {
            0: 'boots',
            1: 'flip_flops',
            2: 'loafers',
            3: 'sandals',
            4: 'sneakers',
            5: 'cleats'
        }
        
        model_path = hf_hub_download(repo_id="eric-solak/ShoeClassificationAI", filename="final_model.pth")

        # Load the model
        self.model = models.densenet201(weights=None)
        self.model.classifier = nn.Linear(1920, 6)
        self.model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
        self.model.eval()
        self.model = self.model.cpu()

        # Define transformation (matching training values)
        self.test_transform = transforms.Compose([
            transforms.Resize((224, 224)), # Input size for model
            transforms.ToTensor(), # Converts image to tensor
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]) # Normalize image
        ])

    def analyze(self, image_path):
        image = Image.open(image_path) 
        image = self.test_transform(image).unsqueeze(0)
        image = image.to('cpu')

        # Inference
        with torch.no_grad():
            outputs = self.model(image)
            _, predicted = torch.max(outputs.data, 1)  # Get the predicted class index

        predicted_class = self.class_labels[predicted.item()]
        return predicted_class
