# Exercises day 4

# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
strings = ['Thirty', 'Days', 'Of', 'Python']
concat_string = " ".join(strings)
print(f"Concatenated {strings}: ", concat_string)

# Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

# Print the variable company using print().
print("Company: ", company)

# Print the length of the company string using len() method and print().
print("Company length: ", len(company))

# Change all the characters to uppercase letters using upper() method.
company = company.upper()
print("Uppercase company: ", company)

# Change all the characters to lowercase letters using lower() method.
company = company.lower()
print("Lowercase company: ", company)

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
company = company.capitalize().title().swapcase()
print("Formatted company: ", company)

# Cut(slice) out the first word of Coding For All string.
cut_company = company[0:6]
print("Cut company: ", cut_company)

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
check = "Coding For All".find("Coding") != -1
print("Check if Coding For All string contains a word Coding?: ", check)

# Replace the word coding in the string 'Coding For All' to Python.
replaced = "Coding For All".replace("Coding", "Python")
print(replaced)

# Split the string 'Coding For All' using space as the separator (split()) .
result = "Coding For All".split(" ")
print(result)

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
result = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(", ")
print(result)

# What is the character at index 0 in the string Coding For All.
result = "Coding For All"[0]
print(result)

# What is the last index of the string Coding For All.
result = "Coding For All"[-1]
print(result)

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
text = "Python For Everyone"
words = text.split()
first_chars = map(lambda word: word[0], words)
acronym = "".join(first_chars)
print("acronym: ", acronym)

# Use index to determine the position of the first occurrence of F in Coding For All.
text = "Coding For All"
f_index = text.index('F')
print("F Index: ", f_index)

# Use rfind to determine the position of the last occurrence of l in Coding For All People.
text = "Coding For All People"
l_rfind = text.rfind("l")
print("L rfind index: ", l_rfind)

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
text = 'You cannot end a sentence with because because because is a conjunction'
target_index = text.find('because')
print("'because' first occurance index: ", target_index)

# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
text = "You cannot end a sentence with because because because is a conjunction"
target_index = text.rfind('because')
print("'because' last occurance index: ", target_index)

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
text = "You cannot end a sentence with because because because is a conjunction"
sliced_target_text = text[30:54]
print("Sliced text: ", sliced_target_text)

# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
text = "You cannot end a sentence with because because because is a conjunction"
target_index = text.find('because')
print("'because' index in text: ", target_index)

# Does ''Coding For All' start with a substring Coding?
text = "Coding For All"
check = text.startswith('Coding')
print("Does 'Coding For All' start with 'Coding'?: ", check)

# Does 'Coding For All' end with a substring coding?
text = "Coding For All"
check = text.endswith("Coding")
print("Does 'Coding For All' start end 'Coding'?: ", check)

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
text = '   Coding For All      '
formatted = text.strip()
print(f"`{text}` with trailing whitespace removed: `{formatted}`")

# Which one of the following variables return True when we use the method isidentifier():
#   30DaysOfPython
#   thirty_days_of_python
str_a = "30DaysOfPython"
str_b = "thirty_days_of_python"
print(f"`{str_a}` is a valid identifier?: {str_a.isidentifier()}")
print(f"`{str_b}` is a valid identifier?: {str_b.isidentifier()}")

# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries_list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
libraries_string = ", ".join(libraries_list)
print("Joined libraries string: ", libraries_string)

# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries_list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
libraries_string = "# ".join(libraries_list)
print("Joined libraries with hash: ", libraries_string)

# Use the new line escape sequence to separate the following sentences.
#   I am enjoying this challenge.
#   I just wonder what is next.
print("I am enjoying this challenge.\nI just wonder what is next.")

# Use a tab escape sequence to write the following lines.
#   Name      Age     Country   City
#   Asabeneh  250     Finland   Helsinki
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

# Use the string formatting method to display the following:
#   radius = 10
#   area = 3.14 * radius ** 2
#   The area of a circle with radius 10 is 314 meters square.
radius = 10
area = 3.14 * radius ** 2
print(f"The are of the circle with radius {radius} is {area} meters square.")
