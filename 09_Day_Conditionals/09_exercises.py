# Exercises: Day 9

# Exercises: Level 1

# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive.
# If below 18 give feedback to wait for the missing amount of years. Output:
age = float(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive")
else:
    age_diff = 18 - age
    print(
        f"You need {age_diff} more year{'s' if age_diff > 1 else ''} to learn to drive")

# Compare the values of my_age and your_age using if … else. Who is older (me or you)?
# Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age,
# 'years' for bigger differences, and a custom text if my_age = your_age. Output:
my_age = 30
your_age = float(input("Enter your age: "))
age_diff = abs(my_age - your_age)
year_word = 'year' if age_diff == 1 else 'years'

if my_age > your_age:
    print(f"I am older than you by {age_diff} {year_word}")
elif your_age > my_age:
    print(f"You are older than me by {age_diff} {year_word}")
else:
    print("We are the same age")


# Get two numbers from the user using input prompt.
# If a is greater than b return a is greater than b,
# if a is less b return a is smaller than b,
# else a is equal to b. Output:

# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3

a = float(input("Enter number one: "))
b = float(input("Enter number two: "))

if a > b:
    print(f"{a} is greater than {b}")
elif b > a:
    print(f"{b} is greater than {a}")
else:
    print(f"The numbers are equal")


# Exercises: Level 2
# Write a code which gives grade to students according to theirs scores:

# 80-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F

# I thought this would be cooler than just doing a series of if statements

score = float(input("Enter your score out of 100: "))

grade_map = {
    10: 'A', 9: 'A', 8: 'A',
    7: 'B',
    6: 'C',
    5: 'D'
}

grade = grade_map.get(score // 10, 'F')

print(f"Your grade is: {grade}")


# Check if the season is Autumn, Winter, Spring or Summer. If the user input is:
# September, October or November, the season is Autumn. December, January or February, the season is Winter.
# March, April or May, the season is Spring June, July or August, the season is Summer

month = input("Enter a month: ").strip().title()

if month in ['September', 'October', 'November']:
    season = 'Autumn'
elif month in ['December', 'January', 'February']:
    season = 'Winter'
elif month in ['March', 'April', 'May']:
    season = 'Spring'
elif month in ['June', 'July', 'August']:
    season = 'Summer'
else:
    season = 'Invalid month'

print(f"The season is {season}")


# The following list contains some fruits:

fruits = ['banana', 'orange', 'mango', 'lemon']

# If a fruit doesn't exist in the list add the fruit to the list and print the modified list.
# If the fruit exists print('That fruit already exist in the list')
fruit = input("Enter your fruit: ").strip().lower()

if fruit in fruits:
    print(f"{fruit} is already in the list")
else:
    fruits.append(fruit)
    print(f"{fruit} has been added to the list: ", fruits)


# Exercises: Level 3

# Here we have a person dictionary. Feel free to modify it!
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
    print(person['skills'][len(person['skills']) // 2])
else:
    print("There are no skills")

#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person and 'Python' in person['skills']:
    print('Asabeneh has skills in python')
else:
    print("Asabeneh doesn't know python")


#  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
frontend = {'JavaScript', 'React'}
backend = {'Node', 'Python', 'MongoDB'}
fullstack = {'React', 'Node', 'MongoDB'}
skills_set = set(person['skills'])

if fullstack.issubset(skills_set):
    print("He is a full stack developer")
elif frontend.issubset(skills_set):
    print("He is a front end developer")
elif backend.issubset(skills_set):
    print("He is a back end developer")
else:
    print("unknown title")

#  * If the person is married and if he lives in Finland, print the information in the following format:
#     Asabeneh Yetayeh lives in Finland. He is married.
if person['is_marred'] == True and person['country'] == 'Finland':
    print(f"{person['first_name']} lives in Finland. He is married")
