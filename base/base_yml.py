import yaml

def yml_data_with_file(filename):
    with open('./data/' + filename + ".yml", "r", encoding="utf-8") as f:
        return yaml.load(f, Loader=yaml.FullLoader)

