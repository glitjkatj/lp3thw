#sys is a python module
#argv() is an array for command line arguments 
from sys import argv

script, first, second, third = argv

print("The name of the script is: ", script)
print("The first variable passed in is: ", first)
print("The second? ", second)
print("The third? ", third)