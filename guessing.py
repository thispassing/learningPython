from random import randint


guess = int(input("Guess a number between 1 and 10: "))
number = randint(1,10)

while guess != number:
    if guess < number:
        guess = int(input("Too low, try again: "))
    elif guess > number:
        guess = int(input("Too high, try again: "))
    if guess == number:
        print("Winner!")
        play_again = input("Do you want to keep playing? (y/n) ")
        play_again = play_again.lower()
        if play_again == "y":
            guess = int(input("Guess a number between 1 and 10: "))
            number = randint(1,10)
        elif play_again == "n":
            print("OK, cya next time!")
        elif play_again == "stop":
            print("OK, I'll stop.")
            break
        else:
            print("Sry, I don't understand that.")

