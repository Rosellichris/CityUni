# Creates a tuple containing multiple data types
courses = ("CS101", 2.0, 3)

# Prints the original tuple
print("Original tuple:", courses)

# Attempts to modify the second element (this will cause an error)
courses[1] = 4.0

# This line will never execute because the line above raises an error
print("Updated tuple:", courses)