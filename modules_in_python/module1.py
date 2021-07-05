import module2
from module2 import add
import json

# Hierarchy
# Standar module: Can't be overwritten
# Working dir
# paths

json.my_module()
# dir c:\Users\Nienke\projects\python_trainning\modules_in_python\json.py
# path C:\Users\Nienke\AppData\Local\Programs\Python\Python37\lib\json\__init__.py
print(json.__file__)

import math
# url: Python standar module: https://docs.python.org/3/library/
print(math.cos(2))
#print(math.__file__) # AttributeError. This file does'n exist.  




# URL: https://www.youtube.com/watch?v=DpRE-UFFnro&list=PLcxbJOVMGpYDYnUsUT8qfQWKz3MpHNFjC&index=26