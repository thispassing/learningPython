squares = []
for x in range(1,12):
    squares.append(x**2)

with open("something.txt", "w") as hehe:
    for y in squares:
            hehe.write(str(y) + "\n")