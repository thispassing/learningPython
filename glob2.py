import glob2
from datetime import datetime

# originally this was filesnames = glob2.glob('*.txt'), but i don't think it worked with all the other .txt
# files in this folder, so i just changed it for now, can test in another location one time

filenames = ['file1.txt', 'file2.txt', 'file3.txt']
with open(datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f"+".txt"), "w") as file:
    for filename in filenames:
        with open(filename, "r") as f:
            file.write(f.read() + "\n")
    