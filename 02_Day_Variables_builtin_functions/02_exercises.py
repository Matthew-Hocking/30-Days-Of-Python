import math
import json

# ------Exercises: Level 1------

print("Day 2: 30 Days of python programming")

# Declare variables
first_name = "Matthew"
last_name = "Hocking"
full_name = first_name + " " + last_name
country = "New Zealand"
city = "Wellington"
age = 30
year = 2025
is_married = False
is_true = True
is_light_on = False
height, hair, eye_color = 183, "Brown", "Steel"

# ------Excercises: Level 2------

# Check data types of variables
print("First name type: ", type(first_name))  # Str
print("Age type: ", type(age))  # Int
print("'Is Married' type: ", type(is_married))  # Bool
print("Height: ", type(height))  # Int

# Compare the length of your first name and your last name
first_name_length = len(first_name)
print("Length of my first name: ", first_name_length)

last_name_length = len(last_name)
print("Length of my last name: ", last_name_length)

# Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4
print(f"Nums: {num_one} and {num_two}")

# Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
print("Total: ", total)

# Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
print("Difference: ", diff)

# Multiply num_two and num_one and assign the value to a variable product
product = num_two * num_one
print("Multiplication: ", product)

# Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
print("Division: ", division)

# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one
print("Remainder: ", remainder)

# Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
print("Exponent: ", exp)

# Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
print("Floor Division: ", floor_division)

# The radius of a circle is 30 meters.
#   Calculate the area of a circle and assign the value to a variable name of area_of_circle
#   Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
#   Take radius as user input and calculate the area.
circle_radius = 30
area_of_circle = math.pi * (circle_radius**2)
circum_of_circle = 2 * math.pi * circle_radius

radius_input = int(input("Input the radius of your circle: "))
area_of_circle_input = math.pi * (radius_input**2)
print(
    f"The area of your circle with radius {radius_input} is: {round(area_of_circle_input, 2)}"
)

# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
user = {}

user["first_name"] = input("What is your first name?: ")
user["last_name"] = input("And what is your last name?: ")
user["country"] = input("What country are you from?: ")
user["age"] = input("How old are you?: ")

print("Your details: ", json.dumps(user, indent=2))

# ------Notes------
# Different ways to concat strings
simple_concat = first_name + " " + last_name

join_concat = " ".join([first_name, last_name])

old_style = "%s %s" % (first_name, last_name)

new_style = "{} {}".format(first_name, last_name)

f_string = f'{first_name} {last_name}'
