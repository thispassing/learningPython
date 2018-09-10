myfile = open("sample.txt")
c = myfile.read()
c = c.splitlines()
for i in c:
    print(i)