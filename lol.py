while True:
    name = input("Enter your name: \n")
    if name.isalpha():
        print("Thank you "+ name)
        break
    else:
        continue
