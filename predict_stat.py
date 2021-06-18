import torch
import numpy as np
def predict_stat(tns_image,img_path,labels_dict, i_model, topk,device):
    ''' Predict the class (or classes) of an image using a trained deep learning model.
    ''' 
    idx_to_class = {str(val): int(key) for key,val in i_model.class_to_index.items()}
    input_tns = tns_image
    input_tns = input_tns.unsqueeze(0)
    input_tns = input_tns.to(device)
    i_model.eval()
    with torch.no_grad():
      logps = i_model.forward(input_tns)  
      logps = logps.to("cpu")
    # Calculate accuracy
      ps = torch.exp(logps)
      probs, classes = ps.topk(topk,sorted=True, dim=1)
    classes = classes.numpy()[0]
    classes = [str(idx_to_class[str(i)]) for i in classes]
    probs = probs.numpy()[0]
    print(f"\n The Predict results are :")
    for i,ps in enumerate(probs):
        lable_name = labels_dict[classes[i]]
        print(f"\n {lable_name:30} : {10*ps:.3f} " )