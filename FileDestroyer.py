__author__ = 'iLTeoooD'
import os

__max = 999999999
path = "";inp = " ";n=0
input("***WARNING: THIS WILL OVERWRITE YOUR FILE, USE AT YOUR OWN RISK***\nPress enter to continue...")
while inp != "":
        inp = input("Insert the path of the file: ")
        if inp == "":
            break
        elif os.path.exists(inp):
            path += inp + ","
        else:
            print("File/path not found.")
split=path.split(",")
print("[INFO]: "+str(len(split)-1) +" file(s) found!")
while n <=0:
    try:
        n = int(input("How many times do you want to overwrite it? "))
    except ValueError:
        print("[ERROR]: Input not valid.")
        n=0
for i in range(n):
    print("[INFO]: Overwrite number: "+str(i+1))
    for link in split[:-1]:
        name=link.split(os.sep)[-1]
        nbyte=os.path.getsize(link)
        f = open(link, "wb")
        print("[INFO]: Overwrite of: " + name + "("+str(nbyte)+"bytes) started!")
        while  nbyte> 0:
            if nbyte > __max:
                f.write(os.urandom(__max))
                nbyte -= __max
            else:
                f.write(os.urandom(nbyte))
                nbyte = 0
        f.close()
        print("[SUCCESS]: Overwrite of: " + name + " completed!")