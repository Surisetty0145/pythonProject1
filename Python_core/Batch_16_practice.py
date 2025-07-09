import datetime
import Python_core
import configparser

config = configparser.ConfigParser()
config.read('C:/Users/DELL/OneDrive/Documents/Config/config_input.ini')
a = config.sections()
a.append('KIRAN')
a.insert(0,'Kiran01')
b = ('batch','16','members')
c = a.append(b)
print(type(a))
print(type(b))
print(type(c))
print(a[-1][0:1])
d = a[-1][0:][2:]
print("relistingtype",type(d))
print("relistingvalue",d)
print(d[-1])
#for i in a:
 #   print(i)
#for j in c:
 #   print(j)
value1 = config['General']['port']
print(value1)
dt = datetime.date.today()
dt1 = datetime.datetime.now()
print(dt)
print(dt1)
print(config.get('General','log_level'))

