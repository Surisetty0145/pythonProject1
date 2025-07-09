import configparser
import math

config = configparser.ConfigParser()
config.read("C:/Users/DELL/OneDrive/Documents/Config/config_input.ini")
con_sec = config.sections()
#con_port = config.get()
#config.items()
#config.options()
all_values={}
for k in con_sec:
    all_values[k] = dict(config.items(k))
    print(all_values)
'''
for i in con_sec:
    if i == 'General':
        conf_port = config.items(i)
        conf_port1 = config.options(i)
        print("keys",conf_port1)
        #print(conf_port[1][1])
        #print(type(conf_port))
        it_leg = len(conf_port)
        #print(len(conf_port[1][1]))
        #print(conf_port)
        for i in range(it_leg):
            #print(conf_port[i])
            items_list = (conf_port[i])
            #print(type(items_list))
            #print(items_list)
            it_list2 = len(items_list)
            for j in range(it_list2):
                print(items_list[j])
#for i in
       # for j in conf_port:
         #   print(i,j)
    '''