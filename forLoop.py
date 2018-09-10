

temperatures = [10, -20, -289, 100]

def writer(temperatures):
    with open("temps.txt", "w")as file:
        for c in temperatures:
            if c > -273.15:
                f = c* 9/5 + 32
                file.write(str(f) + "\n")
            else:
                file.write("Can't do it, bro." + "\n")

writer(temperatures)

# using range, append, and creating new .txt file

squares = []
for x in range(1,12):
    squares.append(x**2)

with open("something.txt", "w") as hehe:
    for y in squares:
            hehe.write(str(y) + "\n")