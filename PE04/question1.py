# PE04 Question 1

guests = ["Alice", "Bob", "Charlie"]

print("Guest List:")
print(guests)

guests[1] = "David"

print("\nUpdated Guest List:")
print(guests)

guests.insert(0, "Emma")
guests.insert(2, "Frank")
guests.append("Grace")

print("\nNew Guest List:")
print(guests)

while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry {removed_guest}, I can't invite you to dinner.")

print("\nGuests still invited:")
print(guests)