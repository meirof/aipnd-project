from PIL import Image
import torch
import numpy as np
def process_image(image_path):
    ##normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406],
    #                             std=[0.229, 0.224, 0.225])
    #test_valid_transforms = transforms.Compose([transforms.Resize(224),
    #                                  transforms.CenterCrop(224),
    #                                  transforms.ToTensor(),
    #                                  normalize])
    #image_tensor = test_valid_transforms(im).float()
    #image_tensor = image_tensor.unsqueeze_(0)
    #input = Variable(image_tensor)
    #input = input.to(device)
    
    #return image_tensor
    ''' Scales, crops, and normalizes a PIL image for a PyTorch model,
        returns an Numpy array
    '''
    im = Image.open(image_path)

    width, height = im.size
    size_r = float(width/height)
    n_width  = 256 if size_r <= 1 else int(round(size_r*256,0))
    n_height = 256 if size_r >= 1 else int(round(256/size_r,0))
    im = im.resize(size=(n_width,n_height))
    width, height = im.size
    center = width/2, height/2
    left, top, right, bottom = center[0]-(224/2), center[1]-(224/2), center[0]+(224/2), center[1]+(224/2)
    im = im.crop((left, top, right, bottom))

    im = np.array(im)
    im = im / 255
    mean = np.array([0.485, 0.456, 0.406])
    std = np.array([0.229, 0.224, 0.225])
    im = (im - mean) / std
    im = im.transpose(2, 0, 1)
    tns_im = torch.from_numpy(im).type(torch.FloatTensor)
    return tns_im