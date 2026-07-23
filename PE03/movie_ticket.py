while True:
    age = input("Enter your age (or type quit to exit): ")

    if age.lower() == "quit":
        break

    age = int(age)

    if age < 3:
        print("Your ticket is free.")
    elif age <= 12:
        print("Your ticket price is $10.")
    else:
        print("Your ticket price is $15.")