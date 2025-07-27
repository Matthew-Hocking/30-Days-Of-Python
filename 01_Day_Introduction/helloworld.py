# Introduction
# Day 1 - 30DaysOfPython Challenge

print(3 + 2)   # addition(+)
print(3 - 2)   # subtraction(-)
print(3 * 2)   # multiplication(*)
print(3 / 2)   # division(/)
print(3 ** 2)  # exponential(**)
print(3 % 2)   # modulus(%)
print(3 // 2)  # Floor division operator(//)

# Checking data types

print(type(10))                  # Int
print(type(3.14))                # Float
print(type(1 + 3j))              # Complex
print(type('Matthew'))          # String
print(type([1, 2, 3]))           # List, an unordered collection to store different data types
print(type({'name':'Matthew'})) # Dictionary, an unordered collection of data in a key value pair format
print(type({9.8, 3.14, 2.7}))    # Set, a collection of data types similar to list and tuple, however, a set is not an ordered collection of items. A set only stores unique items.
print(type((9.8, 3.14, 2.7)))    # Tuple, an ordered collection of different data types like list but tuples can not be modified once they are created. They are immutable.
print(type(3 == 3))              # Bool
print(type(3 >= 3))              # Bool

# Solve the Euclidean distance between two points
p = [2, 3]
q = [10, 8]

solution = ((q[0] - p[0]) ** 2 + (q[1] - p[1]) ** 2) ** 0.5

print(f"The Euclidean distance between points p:{p} and q:{q} is: {round(solution, 2)} units")