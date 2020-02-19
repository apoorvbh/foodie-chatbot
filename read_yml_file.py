import yaml

def read_yml(file_location):
    with open(file_location) as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        values = yaml.load(file, Loader=yaml.FullLoader)
    return values