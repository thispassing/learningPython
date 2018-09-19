import random
import time

print("Rock...")
print("Paper...")
print("Scissors...\n")

player = input("player selects:\n").lower()
choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
time.sleep(1.5)
print(f"computer selects:\n{computer}")
time.sleep(1.5)

if player == computer:
    print("draw")
elif player == "rock" and computer == "scissors":
    print("player wins!")
elif player == "paper" and computer == "rock":
    print("player wins!")
elif player == "scissors" and computer == "paper":
    print("player wins!")
else:
    print("computer wins!")

# xd = input("something:").capitalize()
# print(xd)

