# Sort Tuples by First and Second Values

# Part i - Sort by the first value
def first(n):
    return n[0]

def sort_list_first(tuples):
    return sorted(tuples, key=first)

print("Sorted by first value:")
print(sort_list_first([(5,2), (2,1), (4,4), (3,2), (1,2)]))

# --------------------------------------------------

# Part iii - Sort by the second value
def second(n):
    return n[1]

def sort_list_second(tuples):
    return sorted(tuples, key=second)

print("\nSorted by second value:")
print(sort_list_second([(5,2), (2,1), (4,4), (3,2), (1,2)]))

# --------------------------------------------------

# Demonstrate the error
print("\nDemonstrating the error:")
try:
    print(sort_list_second([(5,2), (2,1), (4,4), (3,2), (1,2), (8,)]))
except IndexError as e:
    print("Error:", e)

# --------------------------------------------------

# Fixed version
def second_fixed(n):
    if len(n) > 1:
        return n[1]
    return n[0]

def sort_list_second_fixed(tuples):
    return sorted(tuples, key=second_fixed)

print("\nFixed version:")
print(sort_list_second_fixed([(5,2), (2,1), (4,4), (3,2), (1,2), (8,)]))