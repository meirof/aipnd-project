from collections import OrderedDict
from torchvision import datasets, transforms,models  
from torch import nn,optim    
import torch
def load_cpt(filepath,device):
    if str(device) == "cpu":
      checkpoint = torch.load(filepath,map_location=str(device))
    else:
      checkpoint = torch.load(filepath)
    my_model = getattr( models,checkpoint['model_name'])
    my_model = my_model(pretrained=True)
    for param in my_model.parameters():
        param.requires_grad = False 
    
    classifier = nn.Sequential(OrderedDict([
                 ('fc1',nn.Linear(checkpoint['input_size'],checkpoint['hidden_layer'])), 
                 ('relu',nn.ReLU()),
                 #('Dropout',nn.Dropout(0.4)),
                 ('fc2',nn.Linear(checkpoint['hidden_layer'],checkpoint['output_size'])),
                 ('output',nn.LogSoftmax(dim=1))]))
    my_model.classifier = classifier
    #my_model.optimizer  = checkpoint['optimizer']
    my_model.load_state_dict(checkpoint['state_dict'])
    my_model.class_to_index = checkpoint['class_to_idx']
    my_model = my_model.to(device)
    print(f"Load Model Hyper paramter Values: \n" 
                f"model_name: {checkpoint['model_name'] }\n"
                f"input_size: {checkpoint['input_size'] }\n"
                f"output_size: {checkpoint['output_size']}\n"
                f"epochs: {checkpoint['epochs'] }")
    return my_model