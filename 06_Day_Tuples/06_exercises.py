# Exercises: Day 6

# Exercises: Level 1

# Create an empty tuple
tpl = ()
tpl = tuple()

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
# NOTE: tuple("string") converts each CHARACTER in the string into separate tuple elements
#   This creates: ("E", "l", "i", "z", "a", "b", "e", "t", "h")
#   This is different from creating a tuple with the whole string as one element
sisters = tuple("Elizabeth")  # ('E', 'l', 'i', 'z', 'a', 'b', 'e', 't', 'h')
brothers = tuple("Megatron")  # ('M', 'e', 'g', 'a', 't', 'r', 'o', 'n')

# NOTE: if a tuple is created as a single string with no commas, it is created as a string instead:
#   so `("Elizabeth") + ("Megatron")` actually creates a string "ElizabethMegatron"
#   so we must use commas even if the tuple is only a single item
sisters = ("Elizabeth",)
brothers = ("Megatron",)

# Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers
print("Siblings: ", siblings)

# How many siblings do you have?
print(f"I have {len(siblings)} siblings")

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ("Paul", "Bridget")
print("My family members: ", family_members)


# Exercises: Level 2

# Unpack siblings and parents from family_members
sister, brother, dad, mum = family_members
print(sister, brother, dad, mum)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("Banana", "Apple", "Orange")
vegetables = ("Carrot", "Pumpkin", "Broccoli")
animal_products = ("Beef", "Chicken", "Fish")

food_stuff_tp = fruits + vegetables + animal_products
print("Food Stuffs tuple: ", food_stuff_tp)

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lst = list(food_stuff_tp)
print("Food Stuff list: ", food_stuff_lst)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle = len(food_stuff_lst) // 2
if len(food_stuff_lst) % 2 == 1: 
  del food_stuff_lst[middle:middle+1]
else:
  del food_stuff_lst[middle-1:middle+1]
print("Middle item(s) sliced out: ", food_stuff_lst)

# Slice out the first three items and the last three items from food_staff_lt list
print("Before: ", food_stuff_tp)
food_stuff_tp = food_stuff_tp[3:]
print("First 3: ", food_stuff_tp)
food_stuff_tp = food_stuff_tp[:-3]
print("Last 3: ", food_stuff_tp)

# Delete the food_staff_tp tuple completely
del food_stuff_tp
