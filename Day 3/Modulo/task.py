user_chosen_number = int(input("Choose a number to check if it is an even or odd number....\n"))

# print(user_chosen_number)
# print(type (user_chosen_number))

if user_chosen_number % 2 == 0:
    print("This is an even Number Dude....")
else:
    print("Odd Number!!!")


print(f"Here is the result as well of the modulo/remainder {user_chosen_number % 2}")
