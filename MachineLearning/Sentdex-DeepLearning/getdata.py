import os

def get(filename):
    script_dir = os.path.dirname(__file__)
    data_path = 'data/'+filename
    abs_file_path = os.path.join(script_dir, data_path)
    return abs_file_path

