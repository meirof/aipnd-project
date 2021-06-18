# Imports here
import torch 
from torchvision import datasets, transforms,models
def load_images( data_dir,mean,std,rotaion=30,resize=244,batch_size=64):

   train_dir = data_dir + '/train'
   valid_dir = data_dir + '/valid'
   test_dir = data_dir  + '/test'

   normalize = transforms.Normalize(mean=mean,std=std)
   
   
   train_transforms = transforms.Compose([transforms.RandomRotation(rotaion),
                                         transforms.Resize(resize),
                                         transforms.RandomResizedCrop(resize),
                                         transforms.RandomVerticalFlip(rotaion),
                                         transforms.ToTensor(),
                                         normalize])
   test_valid_transforms = transforms.Compose([transforms.Resize(224),
                                         transforms.CenterCrop(224),
                                         transforms.ToTensor(),
                                         normalize])
   
   # TODO: Load the datasets with ImageFolder
   
   train_data_datasets = datasets.ImageFolder(train_dir, transform=train_transforms)
   valid_data_datasets = datasets.ImageFolder(valid_dir , transform=test_valid_transforms)
   test_data_datasets = datasets.ImageFolder(test_dir , transform=test_valid_transforms)
   image_datasets = {'training_sets': train_data_datasets,
                     'validation_sets': valid_data_datasets ,
                     'testing_sets': test_data_datasets }
   
   # TODO: Using the image datasets and the trainforms, define the dataloaders
   trainloader = torch.utils.data.DataLoader(train_data_datasets, batch_size=batch_size, shuffle=True)
   validloader  = torch.utils.data.DataLoader(valid_data_datasets, batch_size=batch_size)
   testloader  = torch.utils.data.DataLoader(test_data_datasets, batch_size=batch_size)
   image_data = { "trainloader": trainloader,
                 "validloader": validloader,
                 "testloader": testloader}
   return image_data , image_datasets