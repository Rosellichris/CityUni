# PE04 Question 4

foods = ("Pizza", "Burger", "Salad", "Soup", "Rice")

print("Restaurant Menu:")
for food in foods:
    print(food)

try:
    foods[1] = "Pasta"
except TypeError:
    print("\nPython does not allow tuple items to be changed.")

foods = ("Pizza", "Pasta", "Salad", "Steak", "Rice")

print("\nUpdated Menu:")
for food in foods:
    print(food)