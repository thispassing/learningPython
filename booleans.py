# falsy
if 0:
    print("LOL")
# truthy
if 1:
    print("AHAHA")

animal = input("enter your favorite animal: ")

if animal:
    print(animal + " is my favorite too! xD")
else:
    print("what are you on about mate?")

# empty objects, empty strings, None, and zero are all "falsy"

a = 1
a == 1 # True
a is 1 # True

a = [1,2,3]  # a list of number
b = [1,2,3]
a == b # True
a is b # False

c = b
b == c # True