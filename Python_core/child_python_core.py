import Python_Core
import inspect as ins
from inspect import getmembers, isfunction, ismethod

print(dir(Python_Core))
print(Python_Core.add(5,6))
print(Python_Core.Sub(2,5))
#help(Python_Core)
#method_list = ins.getmembers(Python_Core, ins.ismethod)
#print(method_list)
print(getmembers(ins,isfunction))

