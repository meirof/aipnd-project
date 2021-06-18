from collections import OrderedDict
from logging import exception
from torchvision import datasets, transforms,models  
from torch import nn,optim    
def config_model(trained_model, device, output, 
                  lrn_rate, hidden_units,drop_out=0.25):
    """
      config_model function takes the input arguments and acordingly configure the model 
      input 
    Returns:
    object: the model
    object: the loss criterion
    object: the optimizer
   """

    print(f"\n Choosen pre trained  model: {trained_model}\n")
   
    

    # aet attribute dynamicly 
    my_model = getattr( models,trained_model)
    my_model = my_model(pretrained=True)
       
        

    # Freeze parameters 
    for param in my_model.parameters():
         param.requires_grad = False
  
    try:
      in_features = my_model._modules['classifier'][0].in_features
    except: 
      in_features = my_model._modules['classifier'].in_features

    print(f"The number of in_features are: {in_features}")
    
    my_model.classifier = nn.Sequential(OrderedDict([
                  ('fc1', nn.Linear(in_features, hidden_units)),
                  ('relu', nn.ReLU()),
                  ('dropout', nn.Dropout(drop_out)),
                  ('fc2', nn.Linear(hidden_units, output)),
                  ('output', nn.LogSoftmax(dim=1))]))


    # Only train the classifier parameters, feature parameters are frozen
    optimizer = optim.Adam(my_model.classifier.parameters(), lrn_rate)
    criterion =  nn.NLLLoss()
    my_model.to(device);
    
    model_param =  { "model": my_model, "criterion": criterion, "optimizer" : optimizer}
    
    return model_param