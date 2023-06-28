#this one is like using argv
#def is how you define a function
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#apparently args is pointless and I can just do it like this instead
def print_two_again(arg1, arg2): 
    print(f"arg1: {arg1}, arg2: {arg2}")

#the function below just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

#the function below takes no arguments at all
def print_none():
    print("I got nothin")

print_two("Zed","Shaw")
print_two_again("Zed","Shaw") 
print_one("First!")
print_none()