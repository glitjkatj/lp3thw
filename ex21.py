def add(a, b):
    print(f"Adding {a} and {b}")
    return a + b

def subtract(a, b):
    print(f"Subtracting {b} from {a}")
    return a - b

def multiply(a, b):
    print(f"Multiplying {a} and {b}")
    return a * b

def divide(a, b):
    print(f"Dividing {a} by {b}")
    return a / b #single slash gives a floating num, double slash truncates it

print("Hey, mathheads! Let's do some math!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"""Age: {age} 
          Height: {height} 
          Weight: {weight}
          IQ: {iq}""")

#For the extra credit?
print("Here's a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2)))) #so this matryoshka doll is solved from inside out

print("That becomes: ", what)