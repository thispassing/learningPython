# newer file

temperatures = [10, -20, -289, 100]
def c_to_f(c):
    if c < -273.15:
        return "That temperature doesn't make sense!"
    else:
        f = c* 9/5 + 32
        return f
with open("this.txt", "w") as myfile:
    for y in temperatures:
        x = c_to_f(y)
        myfile.write("%s \n " % x)
    