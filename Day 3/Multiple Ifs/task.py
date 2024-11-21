print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0 # Total bill for Later


if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill += 5
        print(f"So your Bill for now is ${bill}")
    elif age <= 18:
        bill += 7
        print(f"So your Bill for now is ${bill}")
    else:
        bill += 12
        print(f"So your Bill for now is ${bill}")
    # wants_photo_included = input(f"Do you want a photo with the ride?\n y for Yes and n for "no..just the ride Only")
    # wants_photo_included = input("Do you want a photo with the ride?\nEnter 'y' for Yes and 'n' for (No ... just the ride only): ")
    wants_photo_included = input(f"Do you want a photo with the ride?\n y for Yes and n for \"no..just the ride Only\"")

    if wants_photo_included == "y":
        bill += 50
        # print(f"So the total bill to be paid is ${bill }")

    print(f"Your total Bill: ${bill}")

else:
    print("Sorry you have to grow taller before you can ride.")
