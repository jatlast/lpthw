my_name = 'Jason T. Baumbach'
my_age = 49 # for less than a month, anyeay.
my_height = 74 # inches
my_height_cm = my_height * 2.54
my_weight = 175 # lbs or so
my_weight_kg = my_weight / 2.2
my_eyes = 'Hazel'
my_teeth = 'White-ish'
my_hair = 'Brown'
print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches ({my_height_cm}cm) tall.")
print(f"He's {my_weight} pounds ({round(my_weight_kg,2)}kg) heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight}, I get {total}.")

