#imports ths argv list from the sys module
from sys import argv

#lays out what the arguments are
script, filename = argv

#opens the file user specifies from input
txt = open(filename)

#f string that prints out the filename user specified from input
print(f"Here's the file named {filename}:")
print(txt.read()) #reads the document

#user is prompted to input filename again
print("Type the filename again: ")
file_again = input(">> ")

#Opens and reads file
txt_again = open(file_again)
print(txt_again.read())