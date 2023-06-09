from sys import argv
from os.path import exists #returns True if a file exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}:")

# we could do these two on one line, how?
# not sure - open(from_file, 'r') ?
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long") #len() returns the length of a string

print(f"Does the output file exist? {exists(to_file)}")
print("Hit RETURN to continue, or CTRL-C to abort.")
input()

out_file = open(to_file, 'w') 
out_file.write(indata)

print("Alright, all done.") 

out_file.close()
in_file.close()