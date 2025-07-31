# Exercises: Day 8

# Create an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Kenai'
dog['color'] = 'Brown'
dog['breed'] = 'Bernie'
dog['age'] = 7

#   Or

dog = {
  'name': 'Kenai',
  'color': 'Brown',
  'breed': 'Bernie',
  'age': 7
}

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
  'first_name': 'Matthew',
  'last_name': 'Hocking',
  'gender': 'Male',
  'age': 30,
  'married': False,
  'skills': ['Cooking', 'Song writing'],
  'country': 'New Zealand',
  'city': 'Wellington'
}

# Get the length of the student dictionary
print("Student dictionary length: ", len(student))

# Get the value of skills and check the data type, it should be a list
student_skills = student.get('skills')
print("Student skills type: ", type(student_skills))

# Modify the skills values by adding one or two skills
#   A couple ways we can achieve this
student['skills'].extend(['CSS', 'TypeScript'])
student['skills'] += ['HTML', 'JavaScript'] # This is actually the same as .extend()
student['skills'].append('Woodworking') # Good for adding single items, or adding lists within lists
student['skills'].insert(0, 'Python') # For adding elements at a specific index
print(student['skills'])

# Get the dictionary keys as a list
print("Student keys: ", student.keys())

# Get the dictionary values as a list
print("Student values: ", student.values())

# Change the dictionary to a list of tuples using items() method
student_lst = student.items()
print("List of student details: ", student_lst)

# Delete one of the items in the dictionary
del student['skills']
print("Student with skills removed: ", student)

# Delete one of the dictionaries
del student