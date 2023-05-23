my_name = 'Thanos'
my_age = 1000
my_height_in_inches = 79 #inches
my_height_in_cm = my_height_in_inches * 2.54
my_weight_in_lbs = 985 #lbs
my_weight_in_kg = my_weight_in_lbs * 0.45
my_eyes = 'purple'
my_teeth = 'white'
my_hair = 'gray'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height_in_inches} inches tall.")
print(f"That's {my_height_in_cm} in centimeters")
print(f"He's {my_weight_in_lbs} pounds heavy.")
print("That's about {my_weight_in_kg} in kilograms, and crazy heavy whichever unit you use.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} unless Tony's snapped his fingers")

# apparently this is line is tricky
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height_in_inches} and {my_weight_in_lbs}, I get {total}. But I don't know why I'm doing the addition to begin with.")