#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */train.py
#                                                                             
# PROGRAMMER: Meir Ofek
# DATE CREATED: Jun 16 2021                                
# REVISED DATE: Jun 30 2021

# PURPOSE: to estimate the probeblity of image based on saved checkpoiny model from train.py program 
#           the program print the  top top_k ( input arg )  classifications 
#           and print the largest classification which have teh max probability  
#             The program is getting  the follwoing input 
#             --img_file <Fulle path image file name >
#             --cpt checkpoint full path 
#             --top_kTop # of classes probeblity to display 
#             --gpu' Uses GPU True Or False
#             --class_dict  Json Classes names file full path 
# The program   will use the follwoyng functions  
# l set_arg , to validate the input argumetns 
# 2 process_image , to load the image and convert it to tensor matrix 
# 3 load_cpt , to load the checkpoint model based on provided checkpoint file 
# 3 predict_stat , calculate the probeblity of classes and print the top_k  


# Imports python modules

import torch
from args_predict import set_args
from load_cpt import load_cpt
from load_image_prd import process_image
from predict_stat import predict_stat
from load_classes import load_classes

def main():
    
    in_args = set_args()

    print("*************<*****>**************")
    print("Predict program using the paramters :")
    print(in_args)
    print("**************<*****>*************")
    print()
    
    top_k  = in_args.top_k
    img_path = in_args.img_file
    cpt_path = in_args.cpt
    class_dict = in_args.class_dict
       
    # Initialize device
    if (in_args.gpu):
      device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    else:
       device = torch.device("cpu")
    print("The model will run with device : {}".format(device))
    
    
    
    classes_dict = load_classes(file_path=class_dict) 

    # Loading the image and proccessing and convert to tensor 
    print("\nLoad and proccessing teh image ...")
    tns_img = process_image(img_path)  

    # Prepare the model
    print("\nLoading the checkpint for the model ... ")
    chpt_model = load_cpt(filepath=cpt_path,device=device)

    print("\n Calulate the prediction stats ... ") 
    predict_stat(tns_image=tns_img,img_path=img_path,labels_dict=classes_dict,
                 i_model=chpt_model, topk=top_k,device=device)
# Call to main function to run the program
if __name__ == "__main__":
    main()