# while True:
#     print("How many times do I have to tell you?")
#     x = input()
#     print("CLEAN UP YOUR ROOM!\n"*int(x))

# while True:
#     times = input("How many times do I have to tell you? ")
#     times = int(times)
#     for time in range(times):
#         print("CLEAN UP YOUR ROOM!")

while True:
    y = range(1,21)
    for x in y:
        if x == 4 or x == 13:
            print(f"{x} is unlucky")
        elif x % 2 == 1:
            print(f"{x} is odd")
        else:
            print(f"{x} is even")
    break
