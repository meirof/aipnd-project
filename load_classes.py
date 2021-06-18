import json
def load_classes(file_path):
    with open(file_path, 'r') as f:
      cat_to_name = json.load(f)
    return cat_to_name