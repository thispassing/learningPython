# print("Hey, how's it going?")
# line = input()
# while line != "stop copying me":
#     print(line)
#     line = input()
# print("UGH FINE YOU")

# while True:
#     command = input("Type 'exit' to exit: ")
#     if command == "exit":
#         break

# for x in range (1,31):
#     print(x)
#     if x == 3:
#         break

# times = int(input("How many times do I have to tell you? "))
# 
# for time in range(times):
#     print("CLEAN UP YOUR ROOM!")
#     if time >= 3:
#         print("Do you even listen anymore?")
#         break

from random import randint

number = randint(1,10)
i = 1
while number != 5:
    print(f"Line {i}: {number} was selected")
    i += 1
    number = randint(1,10)
    if number == 5:
        break
print(f"Line {i}: Oops, 5 was selected.  Game over.")
