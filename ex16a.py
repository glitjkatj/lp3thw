from sys import argv

script, filename = argv

print("Opening file!")
target = open(filename, 'a')

print("Would you like to append anything to the file? If not press Ctrl+C.")
extra_txt = input(">> ")

target.write(extra_txt)

print("Ok. Goodbye.")
target.close()