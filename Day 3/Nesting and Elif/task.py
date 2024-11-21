print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? \n"))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?"))
    if age == 100:
        print("1000 Fucky")
    elif age == 200:
        print("200 Yeah")
    else:
        print("Noooooo!")
else:
    print("Sorry you have to grow taller before you can ride.")
