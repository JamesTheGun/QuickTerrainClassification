import torch

def load_model():
    model = torch.load('data/model.pth')
    return model

def predict(model, input_data: torch.Tensor):
    pass