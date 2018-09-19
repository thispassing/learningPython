print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("player one pick: ")
player2 = input("player two pick: ")

if player1 == player2:
    print("draw")
elif player1 == "paper" and player2 == "rock":
    print("player one wins!")
elif player1 == "paper" and player2 == "scissors":
    print("player two wins!")
elif player1 == "rock" and player2 == "paper":
    print("player two wins!")
elif player1 == "rock" and player2 == "scissors":
    print("player one wins!")
elif player1 == "scissors" and player2 == "paper":
    print("player one wins!")
elif player1 == "scissors" and player2 == "rock":
    print("player two wins!")
else:
    print("there was an error")

