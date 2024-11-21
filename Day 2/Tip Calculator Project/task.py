print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? \n$"))
tip = int(input("What percentage tip would you like to give? 10 12 15 (%) "))
people = int(input("How many people to split the bill? "))


calculated_tip = bill *(tip/100)
print(calculated_tip)
print(type(calculated_tip))

final_amount_by_each_person = ((bill + calculated_tip) / people)

print(f"Each Person should pay: ${round(final_amount_by_each_person,2)}")

