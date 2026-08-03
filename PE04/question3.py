# PE04 Question 3

numbers = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

duplicates = []

for number in numbers:
    if numbers.count(number) > 1 and number not in duplicates:
        duplicates.append(number)

print("Original list:")
print(numbers)

print("\nDuplicate elements:")
print(duplicates)