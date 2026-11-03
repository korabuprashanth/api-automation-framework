import configparser
from pathlib import Path

config_dir = 'Config'
config_file = 'config.ini'

config = configparser.ConfigParser()
base_dir = Path(__file__).parent.parent
file = base_dir.joinpath(config_dir).joinpath(config_file)
config.read(file)


def get_url(env, service):
    return config[env][service].strip('"')
