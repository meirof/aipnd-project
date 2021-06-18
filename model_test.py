# TODO: Do validation on the test set
import torch
def model_test(model_param,device,data_dict):

   model_param["model"].to(device);
   model_param["model"].eval()
   accuracy = 0
   test_loss = 0
   with torch.no_grad():
      for inputs, labels in data_dict["testloader"]:
           inputs, labels = inputs.to(device), labels.to(device)
           logps = model_param["model"].forward(inputs)
           batch_loss = model_param["criterion"](logps, labels)
   
           test_loss += batch_loss.item()
   
           # Calculate accuracy
           ps = torch.exp(logps)
           top_p, top_class = ps.topk(1, dim=1)
           equals = top_class == labels.view(*top_class.shape)
           accuracy += torch.mean(equals.type(torch.FloatTensor)).item()
   
   print(f"Test Loss: {test_loss/len(data_dict['testloader']):.3f}.. "
        f"Test accuracy: {100*accuracy/len(data_dict['testloader']):.3f} %")