from os.path import exists
file = input("file> ")
if not ".txt" in file[len(file) - 4:len(file)]:
    print("This file is not a Text (.txt) file!")
else:
    if exists(file):
        print(open(file).read())
    else:
        print("File does not exist!")