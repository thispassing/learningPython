# practice with while function using inputs

correct_password = "python123"
name = input("Enter a name: ")
lastname = input("Enter last name: ")
password = input("Enter a password: ")

while password != correct_password:
    password = input("Enter a different password: ")

message = "Hi %s %s, you are logged in.\nPlease continue." % (name,lastname)
print(message)