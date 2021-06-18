#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */train.py
#                                                                             
# PROGRAMMER: Meir Ofek
# DATE CREATED: Jun 14 2021                                
# REVISED DATE: Jun 30 2021

# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The model name his arguments to implemnt the training . 
#            -The no of hidden layers arguamnt hidden_units. 
#            -The no of opochs , epochs 
#            - GPU Fale / True default true , for using the training comuting ,
#            
# The program train.py will use the follwoyng functions  

# Imports python modules
from time import time, sleep
import torch


from args_model_train import set_args
from model_test import model_test
from config_model import config_model
from load_classes import load_classes
from load_images import load_images
from train_nn import train_nn
from save_cpt import save_cpt

def main():
    start_time = time()
    
    in_args = set_args()

    print("********************************")
    print("Training network using the following parameters:")
    print(in_args)
    print("********************************")
    print()
    
    learning_rate = in_args.lrn_rate
    epochs = in_args.epochs
    hidden_units = in_args.hidden_units    
    model_name = in_args.arch
    data_dir   = in_args.dir
    class_dict = in_args.class_dict
    
    # Initialize device
    if (in_args.gpu):
      device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    else:
      device = torch.device("cpu")
    print("The model will run with device : {}".format(device))
    checkpoint_dir = in_args.save_dir+"/"+str(device)+"_checkpoint.cpt"
    mean=[0.485, 0.456, 0.406]
    std=[0.229, 0.224, 0.225]
    
    classes_dict = load_classes(file_path=class_dict) 
    
    # Prepare  the image data and transfer to Tensors with normalization  
    print("\n Start loading and trasfrorm data ... ")
    image_data , image_datasets = load_images( data_dir=data_dir,mean=mean,
                                              std=std,rotaion=30,resize=244,batch_size=64)
    no_of_classes = len(image_datasets["training_sets"].class_to_idx)

    print(f"Number of classes = {no_of_classes}")
    
    # Prepare the model
    print("\n Setting teh model type and paramters ... ")
    model_param = config_model(trained_model=model_name, device=device, output=no_of_classes, 
                        drop_out=0.4, lrn_rate=learning_rate, hidden_units = hidden_units)
    
    # Training the model
    print("\n Starting the Training proccess ...")
    
    train_nn(epochs, data_dict=image_data, device=device, model_param=model_param)
    train_time = time()-start_time
    start_time = time()
    print("\n Train  proccess completed .")
    print("\n** Train Elapsed Runtime:",
          str(int((train_time/3600)))+":"+str(int((train_time%3600)/60))+":"
          +str(int((train_time%3600)%60)) )
    # Test network accuracy
    print("\n Starts the model accuracy testing ...")
    model_test(model_param=model_param,device=device,data_dict=image_data)
    test_time = time() - start_time
    print("\n Model accuracy testing completed ...")
    print("\n** Testing Elapsed Runtime:",
          str(int((test_time/3600)))+":"+str(int(((test_time)%3600)/60))+":"
          +str(int((test_time%3600)%60)) )
    print("\n Started the save_checkpoint  ...")
    # Save checkpoint
    save_cpt(model_param=model_param,checkpoint_dir=checkpoint_dir
                         ,epochs=epochs,image_datasets=image_datasets,lrn_rate=learning_rate,
                         model_name=model_name)
    
   
    total_time = train_time + test_time
    print("\n** Total Elapsed Runtime:",
          str(int((total_time/3600)))+":"+str(int((total_time%3600)/60))+":"
          +str(int((total_time%3600)%60)) )
    
# Call to main function to run the program
if __name__ == "__main__":
    main()