age = input("enter a number: ")
if type(age) == str:
    print("wtf was that")
if int(age) == 21:
    print("you can drink too! super sweet!")
elif int(age) >= 18:
    print("you can vote now")
else:
    print("sry bud")

 #   type(x) == str:
   # print("type a number")