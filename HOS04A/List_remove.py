# Creates a list containing three motorcycle brands
motorcycle = ["Honda", "Yamaha", "Suzuki"]

# Removes the item at index 1 ("Yamaha")
del motorcycle[1]

# Prints the updated list
print(motorcycle)

# Creates another list
motorcycles = ["Honda", "Yamaha", "Suzuki"]

# Removes and stores the last item
popped_motorcycle = motorcycles.pop()

# Prints the updated list
print(motorcycles)

# Prints the removed item
print(popped_motorcycle)

# Removes and stores the first item
first_owned = motorcycles.pop(0)

# Prints the first removed motorcycle
print("The first owned motorcycle is a", first_owned)