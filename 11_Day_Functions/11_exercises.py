import math
import keyword
from collections import Counter, abc

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from data import countries_data

# Exercises: Day 11

# Exercises: Level 1

# Declare a function add_two_numbers. It takes two parameters and it returns a sum.

def add_two_numbers(num1, num2):
    return num1 + num2


print("Add two numbers (2, 3): ", add_two_numbers(2, 3))


# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r):
    return math.pi * r * r


print("Area of cirle with radius 14: ", area_of_circle(14))


# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments.
# Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*nums):
    for num in nums:
        if not isinstance(num, (int, float)):
            return "All arguments need to be numbers"
    return sum(nums)


print("Add all numbers (3,4,5): ", add_all_nums(62, 3, 7))


# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32.
# Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(cels):
    if not isinstance(cels, (int, float)):
        return "Arguments aren't valid celsius values"

    return (cels * 9/5) + 32


print("Convert celsius to fahrenheit (18): ",
      convert_celsius_to_fahrenheit(18))


# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    if not isinstance(month, str):
        return "This value is invalid"

    month_title = month.strip().title()
    season_map = {
        'Autumn': ('September', 'October', 'November'),
        'Winter': ('December', 'January', 'February'),
        'Spring': ('March', 'April', 'May'),
        'Summer': ('June', 'July', 'August')
    }

    for season, months in season_map.items():
        if month_title in months:
            return season

    return "This is not a valid month"


print(check_season('april'))
print(check_season('jUnE'))
print(check_season('wrgert'))
print(check_season(9))


# Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(point1, point2):
    if not isinstance(point1, (tuple, list, set)) or not isinstance(point2, (tuple, list, set)):
        return "These are not valid points"

    x1, y1 = point1
    x2, y2 = point2

    if not all(isinstance(coord, (int, float)) for coord in [x1, y1, x2, y2]):
        return "All coordinates must be numbers"

    if x2 - x1 == 0:
        return "Undefined (vertical line)"
    else:
        return (y2 - y1) / (x2 - x1)


print(calculate_slope((2, 4), (7, 12)))
print(calculate_slope(7, 5))
print(calculate_slope(7, 'Matthew'))
print(calculate_slope(('Matthew', 12), ({}, ())))


# Quadratic equation is calculated as follows: ax² + bx + c = 0.
# Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a, b, c):
    for num in [a, b, c]:
        if not isinstance(num, (int, float)):
            return "All params need to be valid numbers"

    if a == 0:
        return "Not a quadratic equation (a cannot be 0)"

    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        return "No real solutions"
    elif discriminant == 0:
        x = -b / (2*a)
        return f"One solution: x = {x}"
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"Two solutions: x = {x1} and x = {x2}"


print(solve_quadratic_eqn(4, 1, 67))
print(solve_quadratic_eqn(0, 4, 0))
print(solve_quadratic_eqn(4, 6, 0))
print(solve_quadratic_eqn('ma', (), ''))


# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(lst):
    if not isinstance(lst, list):
        return "parameter is not a list"

    return ", ".join(str(lst) for item in lst)


print(print_list([1, 3, 54]))
print(print_list(['foo', 'bar']))
print(print_list({}))


# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
#   NOTE: This function modifies the original list, if i want to return a new list i should just read over the list items backwards, adding them to a new list
def reverse_list(lst):
    if not isinstance(lst, list):
        return "Not a valid list"

    for i in range(len(lst) // 2):
        lst[i], lst[-(i + 1)] = lst[-(i + 1)], lst[i]

    return lst


print(reverse_list([1, 2, 3]))
print(reverse_list([1, 2, 3, 4, 5, 6, 7, 8]))
print(reverse_list(['You', 'and', 'Me']))


# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(lst):
    for item in lst:
        if not isinstance(item, str):
            return "List items must be strings"

    return [item.title() for item in lst]


print(capitalize_list_items(['i', 'like', 'cooking']))
print(capitalize_list_items(['united', 'states', 'of', 'america']))


# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(lst, itm):
    if not isinstance(lst, list):
        return "The list isn't valid"

    return lst + [itm]


food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))


# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(lst, itm):
    if not isinstance(lst, list):
        return "The list isn't valid"

    return [item for item in lst if item != itm]


food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]


# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(num):
    if not isinstance(num, (int)):
        return "Number value is not an integer"

    return sum(range(num + 1))


print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10))  # 55
print(sum_of_numbers(100))  # 5050


# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(num):
    if not isinstance(num, (int)):
        return "Number param is not an integer"

    return sum([n for n in range(num + 1) if n % 2 == 1])


print(sum_of_odds(5))  # 9
print(sum_of_odds(10))  # 25
print(sum_of_odds(100))  # 2500


# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that range.
def sum_of_even(num):
    if not isinstance(num, int):
        return "Number param is not an integer"

    return sum([n for n in range(num + 1) if n % 2 == 0])


print(sum_of_even(5))  #
print(sum_of_even(10))
print(sum_of_even(100))


# Exercises: Level 2

# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
#     print(evens_and_odds(100))
#     # The number of odds are 50.
#     # The number of evens are 51.
def evens_and_odds(num):
    if not isinstance(num, int) or num <= 0:
        return "Number is not a positive integer"

    even_odd_counter = Counter()
    for n in range(num + 1):
        if n % 2 == 0:
            even_odd_counter['even'] += 1
        else:
            even_odd_counter['odd'] += 1

    return f'''
    The number of odds are {even_odd_counter['odd']}.
    The number of evens are {even_odd_counter['even']}.
    '''


print(evens_and_odds(100))
print(evens_and_odds(231))
print(evens_and_odds(12))


# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(num):
    if not isinstance(num, int):
        return "Number is not a whole integer"

    return math.factorial(num)


print(factorial(7))
print(factorial(3))


# Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(arg):
    if not isinstance(arg, abc.Sized):
        return "Argument must be a collection type"

    return len(arg) == 0


print(is_empty(()))
print(is_empty({'thing'}))


# Write different functions which take lists.
# They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
def calculate_mean(nums):
    if not isinstance(nums, list):
        return "Argument must be a list"

    if len(nums) == 0:
        return "Cannot calculate mean of empty list"

    if not all(isinstance(num, (int, float)) for num in nums):
        return "All list items must be numbers"

    return sum(nums) / len(nums)


print(calculate_mean([1, 2, 3, 4, 5]))
print(calculate_mean([132, 122, 37, 42, 200]))
print(calculate_mean([132, 122, 'foo', 'bar']))


def calculate_median(nums):
    # Lets just assume the nums are what we are expecting...
    sorted_nums = sorted(nums)
    middle = len(nums) // 2

    if len(nums) % 2 == 1:
        return sorted_nums[middle]
    else:
        a, b = sorted_nums[middle-1:middle+1]
    return (a + b) / 2


print(calculate_median([132, 122, 37, 42, 200]))
print(calculate_mean([1, 2, 3, 4, 5]))


def calculate_mode(nums):
    # Lets again assume everything is kosher
    data_counter = Counter(nums)
    max_count = data_counter.most_common(1)[0][1]

    modes = [value for value, count in data_counter.items() if count ==
             max_count]

    return modes[0] if len(modes) == 1 else modes


print(calculate_mode([1, 1, 2, 3, 3, 3, 6, 7, 7, 8, 9, 9, 9, 10]))


# Exercises: Level 3

# Write a function called is_prime, which checks if a number is prime.
def is_prime(num):
    if not isinstance(num, int):
        return "You need to provide a whole positive integer"

    if num <= 1:
        return f"{num} is not a prime number"
    if num == 2:
        return f"{num} is a prime number"
    if num % 2 == 0:
        return f"{num} is not a prime number"

    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return f"{num} is not a prime number"

    return f"{num} is a prime number"


print("3: ", is_prime(3))
print("34: ", is_prime(34))
print("3567: ", is_prime(3567))


# Write a functions which checks if all items are unique in the list.
def are_items_unique(lst):
    # Strings are iterable (have a length) so we should also check for this
    if not isinstance(lst, abc.Iterable) or isinstance(lst, str):
        return "Must provide a valid collection type"

    if not lst:
        return "The list is empty"

    return len(lst) == len(set(lst))


print(are_items_unique([1, 2, 3, 3]))
print(are_items_unique('foobar'))
print(are_items_unique([1, 2, 3]))
print(are_items_unique([1, 2, 2, 3, 3]))
print(are_items_unique([]))


# Write a function which checks if all the items of the list are of the same data type.
def are_items_same_type(lst):
    if not isinstance(lst, abc.Iterable) or isinstance(lst, str):
        return "Must provide a valid collection type"

    # So iterators are very cool, and this is pretty clever.
    #   First we create the iterator, it's like a pointer that moves through a collection one item at a time.
    #   Think of it as a bookmark
    #   When an iterator is created, it starts before the first item.
    #   [START] -> 'a' -> 'b' -> 'c' -> [END]
    iterator = iter(lst)
    try:
        # Get the first item and store its type as our reference.
        first_type = type(next(iterator))
    except StopIteration:                 # If there is no first item, then we know the list is empty
        return "The collection is empty"

    # Then, we go through the list and check if the items are the same type, always comparing against the type of the first item
    # And more, the next(iterator) call CONSUMES the first element, so the `for x in iterator` only sees the remaining items
    return all(type(x) == first_type for x in iterator)


print(are_items_same_type([]))
print(are_items_same_type('YOOHOO'))
print(are_items_same_type(99))
print(are_items_same_type([1, 2, {}, 3, 4]))
print(are_items_same_type(['f', 'o', ()]))
print(are_items_same_type(['f', 'o', 'o']))


# Write a function which check if provided variable is a valid python variable
def is_python_variable(var):
    if not isinstance(var, str):
        return f"The variable is not a string type"

    if not var:
        return "The string is empty"

    if not var.isidentifier():
        return f"'{var}' is not a valid identifier"
    elif keyword.iskeyword(var):
        return f"'{var}' is a python keyword and cannot be used as a variable"

    return f"'{var}' is a valid python variable"


print(is_python_variable('_foobar'))
print(is_python_variable('-foobar'))
print(is_python_variable(''))
print(is_python_variable(()))
print(is_python_variable('1foobar'))
print(is_python_variable('dict'))

# Go to the data folder and access the countries-data.py file.

# Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
#   This question is quite unclear.
#   Am i just keeping track of how many times a language occurs in all the data?
#   That's not necessarily the 'most spoken' languages list


def most_spoken_languages(countries, top_num=10):
    language_counter = Counter()

    for country in countries:
        for language in country['languages']:
            language_counter[language] += country['population']

    return language_counter.most_common(top_num)


print(most_spoken_languages(countries_data))
print(most_spoken_languages(countries_data, 20))


# Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
def most_populated_countries(countries, top_num=10):
    pop_dict = {}

    for country in countries:
        pop_dict[country['name']] = country['population']

    return dict(sorted(pop_dict.items(), key=lambda x: x[1], reverse=True)[:top_num])


print("Most Populated Countries")
print(most_populated_countries(countries_data, 20))
