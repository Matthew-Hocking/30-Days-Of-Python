import math

# Exercises day 3

# Declare your age as integer variable
age = 30

# Declare your height as a float variable
height = 183.0

# Declare a variable that store a complex number
complex_var = 4j + 5

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
triangle_base = float(input("Enter base: "))
triangle_height = float(input("Enter height: "))
triangle_area = 0.5 * triangle_base * triangle_height
print(f"The area of the triangle is {round(triangle_area, 2)}")

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
triangle_perimeter = a + b + c
print(f"The area of the triangle is {round(triangle_perimeter, 2)}")

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
rec_length = float(input("Enter length: "))
rec_width = float(input("Enter width: "))
rec_area = rec_length * rec_width
rec_perimeter = 2 * (rec_length + rec_width)
print(f"""The area of the rectangle is {round(rec_area, 2)}
and the perimeter is {round(rec_perimeter, 2)}""")

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
circle_radius = float(input("Enter the radius: "))
circle_area = math.pi * circle_radius * circle_radius
circle_circumference = 2 * math.pi * circle_radius
print(f"""The area of the circle is {round(circle_area, 2)}
and the circumference is {round(circle_circumference, 2)}""")

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
slope_a = 2
print(f"Slope of `y = 2x -2`: {slope_a}")

# Y-intercept: set x = 0
y_intercept = 2 * 0 - 2
print(f"Y-intercept: {y_intercept}")

# X-intercept: set y = 0 and solve for x
x_intercept = 1
print(f"X-intercept: {x_intercept}")

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
a = (2, 2)
print("Point a: ", a)

b = (6, 10)
print("Point b: ", b)

slope_b = (b[1] - a[1]) / (b[0] - a[0])
print("Slope of points 'a' and 'b': ", slope_b)

euclid_dist = ((b[1] - a[1]) ** 2 + (b[0] - a[0]) ** 2) * 0.5
print("The Euclidean distance of points 'a' and 'b': ", euclid_dist)

# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
print("""Solve y:
y = x^2 + 6x + 9""")
x = -5
y = x**2 + 6*x + 9
print(f"When x = -5, y = {y}")

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
p_len = len("Python")
d_len = len("Dragon")

print("'Python' and 'Dragon' aren't the same length: ", p_len != d_len)

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("'on' in 'python' and 'dragon'?: ",
      'on' in 'python' and 'on' in 'dragon')

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = "I hope this course is not full of jargon"
print(f"'jargon' is in the sentence - {sentence}: ", "jargon" in sentence)

# There is no 'on' in both dragon and python
print("There is no 'on' in both dragon and python?: ",
      'on' not in 'python' and 'on' not in 'dragon')

# Find the length of the text python and convert the value to float and convert it to string
text = 'python'
print("Text: ", text)

t_length = len(text)
print("Length: ", len)

t_float = float(t_length)
print("Float: ", float)

string = str(t_float)
print("String: ", string)

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
test_number = float(input("Enter a number: "))
print("Is your number divisible by 2?: ", test_number % 2 == 0)

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
result = 7 // 3 == int(2.7)
print("Check if the floor division of 7 by 3 is equal to the int converted value of 2.7?: ", result)

# Check if type of '10' is equal to type of 10
print("Check if type of '10' is equal to type of 10", type('10') == type(10))

# Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = float(input("Enter your hours: "))
rate = float(input("Enter your rate per hour: "))
print("Your weekly earning is ", hours * rate)

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = float(input("Enter number of years you have lived: "))
seconds = years * 60 * 60
print(f"You have lived for {round(seconds, 1)} seconds")

# Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

for n in range(1, 6):
    print(n, 1, n, n**2, n**3)
