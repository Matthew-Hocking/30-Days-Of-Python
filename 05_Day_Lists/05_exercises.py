import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from data import countries

# Exercises Day 5

# Exercises: Level 1

# Declare an empty list
lst = []
lst = list()

# Declare a list with more than 5 items
lst = [1, 2, 3, 4, 5]

# Find the length of your list
print("Length of lst: ", len(lst))

# Get the first item, the middle item and the last item of the list
skipped_lst = lst[::2]  # Get every second list item
print("Skipped list items: ", skipped_lst)

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Matthew", 30, 183, False, "Wellington"]

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft",
                "Apple", "IBM", "Oracle", "Amazon"]

# Print the list using print()
print("IT Companies: ", it_companies)

# Print the number of companies in the list
print("Number of IT Companies: ", len(it_companies))

# Print the first, middle and last company
# Since we have 7 items in the list we can grab every third item and get the correct first, middle, and last
target_items_list = it_companies[::3]
print("First, Middle, and Last Company: ", target_items_list)

# Print the list after modifying one of the companies
it_companies[0] = "Xero"
print("Replace Facebook with Xero: ", it_companies)

# Add an IT company to it_companies
it_companies.append("Facebook")
print("Add IT Company to list: ", it_companies)

# Insert an IT company in the middle of the companies list
it_companies.insert(4, "Meta")
print("New Company in middle of list: ", it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[3] = it_companies[3].upper()
print("The fourth item is uppercased: ", it_companies)

# Join the it_companies with a string '#;  '
it_company_str = "#; ".join(it_companies)
print("IT Companies joined by `#; `: ", it_company_str)

# Check if a certain company exists in the it_companies list.
print("IBM is in the IT Company list: ", "IBM" in it_companies)

# Sort the list using sort() method
it_companies.sort()
print("The IT Companies are sorted: ", it_companies)

# Reverse the list in descending order using reverse() method
it_companies.reverse()
print("The IT Companies are reversed: ", it_companies)

# Slice out the first 3 companies from the list
sliced_companies = it_companies[0:3]
print("The first 3 items from the list: ", sliced_companies)

# Slice out the last 3 companies from the list
sliced_companies = it_companies[-3:]
print("The last 3 companies: ", sliced_companies)

# Slice out the middle IT company or companies from the list
middle = len(it_companies) // 2
# Example of using a ternery to grab either the one or two middle items based on list length
middle_items = it_companies[middle:middle+1] if len(
    it_companies) % 2 == 1 else it_companies[middle-1:middle+1]
print("The middle items from the Companies list: ", middle_items)

# Remove the first IT company from the list
#   Can be done with .pop() or with del
lst_copy = it_companies.copy()
lst_copy.pop(0)
print("First item revoved using `.pop()`: ", lst_copy)

lst_copy = it_companies.copy()
del lst_copy[0]
print("First item removed using `del`; ", lst_copy)

# Remove the middle IT company or companies from the list
middle = len(it_companies) // 2

if len(it_companies) % 2 == 1:
    del it_companies[middle-1:middle+1]
else:
    del it_companies[middle:middle+1]

print("List with middle item(s) removed: ", it_companies)

# Remove the last IT company from the list
del it_companies[-1]
print("IT Companies with the last item removed: ", it_companies)

# Remove all IT companies from the list
it_companies.clear()
print("IT Companies list is empty: ", it_companies)

# Destroy the IT companies list
del it_companies

# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

simple_join = front_end + back_end
print("A simple join of the two lists: ", simple_join)

front_end.extend(back_end)
print("Join the two lists using `.extend()` method: ", front_end)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = front_end.copy()
redux_index = full_stack.index("Redux")
full_stack.insert(redux_index + 1, "Python")
full_stack.insert(redux_index + 2, "SQL")
print("Fullstack with items inserted after 'Redux': ", full_stack)


# Exercises: Level 2

# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
print("Sorted ages: ", ages)

# There are a number of ways to get the min and max (first and last) items from our list!
#   Simple
min_max_ages = [ages[0], ages[-1]]

#   Slicing with step
min_max_ages = ages[::len(ages)-1]

#   Unpacking first and last items
youngest, *rest, oldest = ages
min_max_ages = [youngest, oldest]


# Find the median age (one middle item or two middle items divided by two)
middle = len(ages) // 2
median_age = 0
if len(ages) % 2 == 1:
    # if the list is odd, grab the middle age
    median_age = ages[middle]
else:
    # if the list is even, grab the middle two and divide the sum of the two middle ages by 2
    median_age = (ages[middle-1] + ages[middle]) / 2

print("The median age of the ages list: ", median_age)


# Find the average age (sum of all items divided by their number )
average_age = sum(ages) / len(ages)
print("The average age is: ", average_age)

# Find the range of the ages (max minus min)
age_range = ages[-1] - ages[0] # this only works if the ages list is sorted (which is it), otherwise...
age_range = min(ages) - max(ages) # ...this is fool proof
print("The range of the ages is: ", age_range)

# Compare the value of (min - average) and (max - average), use abs() method
min_to_avg = abs(min(ages) - average_age)
max_to_avg = abs(max(ages) - average_age)

print(f"Distance from min to average: {min_to_avg}")
print(f"Distance from max to average: {max_to_avg}")

# Find the middle country(ies) in the countries list
middle = len(countries) // 2
middle_countries = countries[middle:middle+1] if len(countries) % 2 == 1 else countries[middle-1:middle+1]
print("Middle Country(s): ", middle_countries)

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
middle = (len(countries) + 1) // 2
countries_a = countries[:middle]
countries_b = countries[middle:]

print("First half length: ", len(countries_a))
print("Second half length: ", len(countries_b))

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
lst = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
china, russia, usa, *scandic = lst