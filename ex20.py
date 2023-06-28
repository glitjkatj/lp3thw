from sys import argv

script, input_file = argv

#the argument f is something we pass in when we call the function
#f isn't a variable that we haven't defined
def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0) #the seek() method changes the position of the file handle to where we specify

def print_a_line(line_count, f):
    print(line_count, f.readline()) #readline() returns one line from a file

current_file = open(input_file)

print("Let's print the whole file:")
print_all(current_file)

print("Now let's rewind:")
rewind(current_file)

print("Let's print 3 lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)



