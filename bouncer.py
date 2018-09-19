# ask for age, 18-21 wristband, 21+ drink, otherwise too young

from time import time

age = input("How old are you: ")
if age:
    age = int(age)
    if age >= 18 and age < 21:
         print("You can enter, but need a wristband.")
    elif age >= 21:
        print("You can enter and drink.")
    else:
        print("Sorry, you may not enter.")
else:
    print("Please enter an age.")
    age = input("How old are you, damnit: ")
