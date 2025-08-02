from collections import Counter
from data import countries, countries_data
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


# Exercises: Day 10

# Exercises: Level 1

# Iterate 0 to 10 using for loop, do the same using while loop.
for number in range(10):
    print("Number: ", number)
else:
    print("For loop completed")

count = 0
while count < 10:
    print("Count: ", count)
    count += 1
else:
    print("While loop complete")

# Iterate 10 to 0 using for loop, do the same using while loop.
for number in range(10, 0, -1):
    print("Number:", number)
else:
    print("For loop completed")

count = 10
while count > 0:
    print("Count:", count)
    count = count - 1
else:
    print("Whilte loop complete")

# Write a loop that makes seven calls to print(), so we get on the output the following triangle:
#   #
#   ##
#   ###
#   ####
#   #####
#   ######
#   #######
for i in range(1, 8):
    print('#' * i)


# Use nested loops to create the following:
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
for row in range(8):
    for col in range(8):
        print('# ', end=' ')
    print()

# Print the following pattern:
# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100
for number in range(11):
    print(f"{number} x {number} = {number*number}")


# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
lst = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for item in lst:
    print(item)

# Use for loop to iterate from 0 to 100 and print only even numbers
#   two ways of doing this, either having an if statement that only prints if even...
for number in range(101):
    if number % 2 == 0:
        print(number)

# Or, use the start, stop, and step parameters
for number in range(0, 101, 2):
    print(number)

# Use for loop to iterate from 0 to 100 and print only odd numbers
#   Similar for this...
for number in range(101):
    if number % 2 != 0:
        print(number)

for number in range(1, 101, 2):  # but here we start from 1 and get every second (odd) number
    print(number)


# Exercises: Level 2

# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# The sum of all numbers is 5050.
total_sum = 0
for number in range(101):
    total_sum += number
print(total_sum)


# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
# The sum of all evens is 2550. And the sum of all odds is 2500.
total_even = 0
total_odd = 0

for number in range(101):
    if number % 2 == 0:
        total_even += number
    else:
        total_odd += number

print("Total even sum:", total_even)
print("Total odd sum:", total_odd)


# Exercises: Level 3

# Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
land_countries = list()

for country in countries:
    if 'land' in country.lower():
        land_countries.append(country)
print("Countries containing land", land_countries)

# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
#   There are a couple ways to solve this.
#   i.e. you have a new 'reversed_fruits' list and always add the fruit in the first index
#   or iterating backwards through the list and adding to the new.
#   but i thought this was pretty clever
fruits = ['banana', 'orange', 'mango', 'lemon']

# We only iterate through the first half of the list, as we will swap them with the other half.
# Regardless of list length this will always get the first half, even if there is an odd number, the center will be ignored.
for i in range(len(fruits) // 2):
    # Then we say the fruit is swapped with it's negative indexed counterpart, and so on as we iterate.
    # We swap fruits[0] with fruits[-1], fruits[1] with fruits[-2], etc.
    fruits[i], fruits[-(i + 1)] = fruits[-(i + 1)], fruits[i]
print("Fruits list reversed in for loop: ", fruits)

# Go to the data folder and use the countries_data.py file.

# What are the total number of languages in the data
#   Question: do they want unique count, or total count? lets figure out both.

# Total count not including duplicates
total_count = 0
for country in countries_data:
    total_count += len(country['languages'])

# Or in a shorter format
total_count = sum(len(country['languages']) for country in countries_data)

print("Total number of languages across all countries:", total_count)

# Total unique count of countries, ingoring duplicates
languages_set = set()
for country in countries_data:
    languages_set.update(country['languages'])

# Or using set comprehension and nested for loops
unique_languages = {
    lang for country in countries_data for lang in country['languages']}
# what we're seeing here is a shorthand for nested for loops. kind of like...
#   for country in countries_data:
#     for lang in country['languages']:
#       languages_set.add(lang)
# and since this is all in a set, we only store the unqie values.

unique_count = len(unique_languages)

print("The number of unique languages across all countries: ", len(languages_set))

# Find the ten most spoken languages from the data
#   A couple ways to do this...
language_dct = {}

for country in countries_data:
    for lang in country['languages']:
        if lang in language_dct:
            language_dct[lang] += 1
        else:
            language_dct[lang] = 1

# So this sorting code looks foreign...
top_10 = sorted(language_dct.items(), key=lambda x: x[1], reverse=True)[:10]
# Here's how it works...
#   language_dct.items() returns us something like
#     [('English', 12), ('Mandarin', 14), ('Russian', 2)...]
#     a list of tuples with effectively name and count values
#   This key=lambda x: x[1] is the tricky part: its a nameless function that takes an input `x` and returns x[1]
#   We want to sort the results by their count, so we access the second elementt in the tuple with index 1.
#   So this function is telling our sorted function to sort these tuples by their second element.
#   By default sorted() sorts items from smallest to largest, so we want to reverse that.
#   Finally, [:10] is then grabbing the first 10 elements of that sorted result

print("Top 10 using dictionary and sorted method")
for lang, count in top_10:
    print(f"{lang}: {count} countries")

#   Or...
language_counter = Counter()
for country in countries_data:
    for lang in country['languages']:
        language_counter[lang] += 1

top_10 = language_counter.most_common(10)
print("Top 10 using the Counter method and inbuilt most_common method")
for lang, count in top_10:
    print(f"{lang}: {count} countries")

# Find the 10 most populated countries in the world
population_dict = {}
for country in countries_data:
    population_dict[country['name']] = country['population']

top_10 = sorted(population_dict.items(), key=lambda x: x[1], reverse=True)[:10]
print("Top 10 countries by population")
for name, population in top_10:
    print(f"{name}: {population}")
