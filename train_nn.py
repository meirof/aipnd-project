import torch
def train_nn(epochs, data_dict, device, model_param):
  steps = 0
  running_loss = 0
  print_every = 10
  train_losses, valid_losses = [], []
  for epoch in range(epochs):
    for inputs, labels in data_dict["trainloader"]:
        steps += 1
        # Move input and label tensors to the default device
        inputs, labels = inputs.to(device), labels.to(device)
       
        model_param["optimizer"].zero_grad()
        
        logps = model_param["model"].forward(inputs)
        loss = model_param["criterion"](logps, labels)
        
        loss.backward()
        model_param["optimizer"].step()

        running_loss += loss.item()

        if steps % print_every == 0:
           valid_loss = 0
           accuracy = 0
           model_param["model"].eval()
           with torch.no_grad():
             for inputs, labels in data_dict["validloader"]:
                  inputs, labels = inputs.to(device), labels.to(device)
                  logps = model_param["model"].forward(inputs)
                  batch_loss = model_param["criterion"](logps, labels)
  
                  valid_loss += batch_loss.item()
                   
                  # Calculate accuracy
                  ps = torch.exp(logps)
                  top_p, top_class = ps.topk(1, dim=1)
                  equals = top_class == labels.view(*top_class.shape)
                  accuracy += torch.mean(equals.type(torch.FloatTensor)).item()
           train_losses.append(running_loss/len(data_dict["trainloader"]))
           valid_losses.append(valid_loss/len(data_dict["validloader"]))

           print(f"Epoch {epoch+1}/{epochs}.. "
                f"Train loss: {running_loss/print_every:.3f}.. "
                f"Validation loss: {valid_loss/len(data_dict['validloader']):.3f}.. "
                f"Validation accuracy: {100*accuracy/len(data_dict['validloader']):.3f}%")
           running_loss = 0
           model_param["model"].train()
                
#plt.plot(train_losses, label = 'Training loss')
#plt.plot(valid_losses, label = 'Validation loss')
#plt.legend(frameon = False)
