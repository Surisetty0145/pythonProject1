import configparser
from inspect import getmembers, isfunction, ismethod


print(getmembers(configparser,ismethod))
help(configparser)
config = configparser.ConfigParser()
config.read("C:/Users/DELL/OneDrive/Documents/Config/config_input.ini")
con_sec = config.sections()

for sections in con_sec:
    for key,values in config.items(sections):
        print(f"options:{key},values:{values}")
