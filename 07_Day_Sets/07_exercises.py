# Exercises: day 7

# sets
it_companies = {'Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercises: Level 1

# Find the length of the set it_companies
print("Length of IT Companies: ", len(it_companies))

# Add 'Twitter' to it_companies
it_companies.add("Xero")
print("Add 'Xero' to the IT Companies list: ", it_companies)

# Insert multiple IT companies at once to the set it_companies
it_companies.update(['Meta', 'PaySauce'])
print("Add multiple Companies to the set: ", it_companies)

# Remove one of the companies from the set it_companies
it_companies.remove('PaySauce')
print("Remove Paysauce from IT Companies: ", it_companies)

# What is the difference between remove and discard
#   .remove() will throw an error if the element isn't a member of the set.
#   .discard() will do nothing if the element isn't a member of the set.


# Exercises: Level 2

# Join A and B
AB = A.union(B)
print("Combaine the two sets A and B: ", AB)

# Find A intersection B
print("Common elements between sets A and B: ", A.intersection(B))

# Is A subset of B
print("Is A a subset of B?: ", A.issubset(B))

# Are A and B disjoint sets
print("Are A and B disjoint sets?: ", A.isdisjoint(B))

# Join A with B and B with A
AB = A.union(B)
BA = B.union(A)
print("Join A with B: ", AB)
print("Join B with A: ", BA)

# What is the symmetric difference between A and B
print("Symetric difference between A and B: ", A.symmetric_difference(B))

# Delete the sets completely
del A
del B


# Exercises: Level 3

# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_st = set(age)
print("Length of age list: ", len(age))  # 8
print("Length of age set: ", len(age_st))  # 5

# Explain the difference between the following data types: string, list, tuple and set
#   String: is a sequence of characters
#   List: is a collection which is ordered and changeable, allows duplicate members
#   Tuple: is a collection which is ordered and unchangeable.
#   Set: is a collection which is unordered and unchangeable but we can add to it, it does not allow duplicates

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

text = "I am a teacher and I love to inspire and teach people."
text_lst = text.split(" ")
text_st = set(text_lst)
print("Unique characters in text: ", text_st)