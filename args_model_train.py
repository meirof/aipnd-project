  
import argparse

def set_args():
    """
     Validate the train.py argument running from command line 
    """
   
    parser = argparse.ArgumentParser()

    parser.add_argument('--dir', required = True,type = str, help = 'python train.py --dir data_directory') 
    parser.add_argument('--arch', type = str, default = 'vgg16',choices = ['vgg16','densenet121'], help = 'Choose Pre Trained model name') 
    parser.add_argument('--lrn_rate', type = float, default = 0.001, help = 'Learning rate')
    parser.add_argument('--hidden_units', type = int, default = 1024, help = 'Hidden units')
    parser.add_argument('--epochs', type = int, default = 4, help = 'No of  epochs')
    parser.add_argument('--gpu',type=bool, default = False, 
                        help = 'Use this argument to start using GPU else don\'t use it.')
    parser.add_argument('--save_dir', type = str, default = './', help = 'Set directory to save checkpoints') 
    parser.add_argument('--class_dict', type = str, default = "cat_to_name.json" ,
                         help = ' Json Classes names file full path  ')
    
    return parser.parse_args()