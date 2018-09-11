def divide(a,b):
        return a/b

x = int(input("type in 1 numbers: "))
y = int(input("type another: "))

while y == 0:
    print("Your second input is 0, mate.\nIs problem.\nBig Facts.")
    y = int(input("type another again: "))
else:
    print("first number/second number =", divide(x,y))