# Creates a list containing positive and negative numbers
original = [8, 20, -10, 55, -777]

# Prints each element in the original list
for i in original:
    print(i)

# Replaces negative numbers with positive numbers
for i in range(len(original)):
    if original[i] < 0:
        original[i] = abs(original[i])

# Prints the modified list
print("Modified list:", original)