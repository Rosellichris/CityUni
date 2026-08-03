# HOS04A Lists - Creating, accessing, updating, and adding values

list1 = ["physics", "chemistry", 1997, 2000]  # Creates a list with different data types
list2 = [1, 2, 3, 4, 5]  # Creates a list of numbers

print("list1[01: ", list1[0])  # Prints the first item in list1
print("list2[1:5]: ", list2[1:5])  # Prints items from index 1 to index 4

print(f"Value before update: {list2}")  # Displays list2 before changing a value
list2[2] = 10  # Updates the value at index 2
print(f"Value after update: {list2}")  # Displays list2 after the update

list1.append(2020)  # Adds a new value to the end of the list
print("new list:", list1)  # Prints the list after append

list1.insert(0, "Python")  # Adds a new value at index 1
print("After insert: ", list1)  # Prints the list after insert

