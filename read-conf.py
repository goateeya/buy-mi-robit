import configparser as cp

def load_profile(file, section):
    section = str(section).upper()
    config = cp.ConfigParser()
    config.read(file)
    return config[section]
