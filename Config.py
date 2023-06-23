import yaml


config_file_name = "C:\\Users\\pratik\\Desktop\\REST_API\\ConfigFile.yaml"
with open(config_file_name) as file:
    app_params = yaml.load(file, Loader=yaml.FullLoader)