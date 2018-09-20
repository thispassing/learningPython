from random import randint


guess = None
number = randint(1,10)

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < number:
        print("Too low, try again.")
    elif guess > number:
        print("Too high, try again.")
    else:
        print("Winner!")
        play_again = input("Do you want to keep playing? (y/n) ")
        play_again = play_again.lower()
        if play_again == "y":
            number = randint(1,10)
        elif play_again == "n":
            print("OK, cya next time!")
            break
        elif play_again == "stop":
            print("OK, I'll stop.")
            break
        else:
            print("Sry, I don't understand that.")
            continue
