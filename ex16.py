from sys import argv

script, filename = argv

print(f"Do you want to erase {filename}?")
print("If you don't want that, hit CTRL-C.")
print("If you do want that, hit RETURN.")

input("? ")

print("Opening file!")
target = open(filename, 'w')

print("Truncating the file!")
target.truncate()

print("Type in 3 lines.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("Writing these lines to the file.")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("We're closing the file.")
target.close()
