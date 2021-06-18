import torch
def save_cpt(model_param,checkpoint_dir,epochs,image_datasets,lrn_rate,model_name):
# TODO: Save the checkpoint
  in_features = model_param["model"]._modules['classifier'][0].in_features
  hidden_layer = model_param["model"]._modules['classifier'][0].out_features
  output = model_param["model"]._modules['classifier'][3].out_features

  checkpoint = {'state_dict': model_param["model"].state_dict(),
                'input_size': in_features,
                'hidden_layer': hidden_layer,
                'output_size': output, 
                'epochs': epochs,
                'learning_rate': lrn_rate,
                'class_to_idx': image_datasets["training_sets"].class_to_idx,
                'classifier': model_param["model"].classifier,
                'optimizer': model_param["optimizer"].state_dict(),
                'model_name': model_name }
  #Save chesckpoint
  torch.save(checkpoint, checkpoint_dir)
  print(f"\n the checkpoint file saved as {checkpoint_dir}")