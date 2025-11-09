"""
3. Module Import Styles
Write a program that demonstrates the different ways to import:
import module_name
from module_name import function_name
from module_name import *
import module_name as alias
Use a module (either built-in like math or your custom module mymath) to show each import style in action.
"""
print("------import math_random----")
import math_random
math_random.modules_demo()

print("------from math_random import  Random_integer----")
from math_random import  Random_integer
Random_integer()

print("------from math_random import *----")
from math_random import *
ceil_and_floor()

print("------import modules as modu----")
import modules as modu
modu.sample()