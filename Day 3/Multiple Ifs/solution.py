print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? \n"))
bill = 0 # Total bill for Later

if height >= 120:
    print("You Can Ride")
    age = int(input("And What is your age?... \n"))
    if age <12:
        new_bill = bill +5
        print(f"Your total bill will be ${new_bill}")
    elif age <=18:
        new_bill = bill + 7
        print(f"Your total bill will be ${new_bill}")
    else:
        new_bill = bill + 12
        print(f"Your total bill will be ${new_bill}")
    need_photos= input("So ... Do you Need Photos? (y/n) \n")
    if need_photos == "y":
        bill_plus_photos = new_bill +3
        print(f"The total bill is ${bill_plus_photos}")
    else:
        print(f"Total bill is ${new_bill}")
else:
    print("You can't ride this game!")