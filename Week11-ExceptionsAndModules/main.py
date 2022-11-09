import random
import cup

#  from module name import classname
from cup import Cup

# module name . function or class name
cup = cup.Cup(100)

cup = Cup(100)

while True:
    try:
        to_add = int(input("How many milliliters do you want to add?"))
        cup.add_liquid(to_add)
        break
    except ValueError as e:
        print(e)

