  
import argparse

def set_args():
    """
     Validate the train.py argument running from command line 
    """
   
    parser = argparse.ArgumentParser()

    parser.add_argument('--img_file', required = True,type = str, help = ' <Fulle path image file name >') 
    parser.add_argument('--cpt', required = True,type = str, help = 'checkpoint full path ') 
    parser.add_argument('--top_k',default = 5 ,type = int, help = 'Top # of classes probeblity to display ') 
    parser.add_argument('--gpu',type=bool, default = False, 
                        help = 'Use this argument to start using GPU else don\'t use it.')
    parser.add_argument('--class_dict', type = str, default = "cat_to_name.json" , 
                         help = ' Json Classes names file full path  ')
    
    return parser.parse_args()
