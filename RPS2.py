print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("player one pick: ")
print("No cheating!\n\n" * 20)
player2 = input("player two pick: ")

if player1 == player2:
    print("draw")
elif player1 == "rock":
    if player2 == "scissors":
        print("player1 wins!")
    elif player2 == "paper":
        print("player2 wins!")
    else:
        print("something went very wrong")
elif player1 == "paper":
    if player2 == "scissors":
        print("player2 wins!")
    elif player2 == "rock":
        print("player1 wins!")
    else:
        print("something went very wrong")
elif player1 == "scissors":
    if player2 == "rock":
        print("player2 wins!")
    elif player2 == "paper":
        print("player1 wins!")
    else:
        print("something went very wrong")           
else:
    print("something went very wrong")