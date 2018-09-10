# random

import random

for i in range(5):
    print(random.random())


# printing numbers into a .txt file

numbers = [1,2,3]
file = open("numbers.txt", "w")
for y in numbers:
    file.write(str(y) + "\n")
file.close()