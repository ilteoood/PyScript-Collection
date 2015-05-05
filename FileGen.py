__author__ = 'iLTeoooD'
import os

__max = 999999999


def __inputcheck(msg, n=0):
    while n <= 0:
        try:
            n = int(input(msg))
        except ValueError:
            print("[ERROR]: Input not valid.")
            n = 0
    return n

if __name__=="__main__":
    n = __inputcheck("How many file do you want to create? ")
    nome = input("Base name? ")
    extension = input("Extension? ")
    if not extension.startswith("."):
        extension = "." + extension
    nbyte = __inputcheck("Dimension? (In byte) ")
    nbyte_temp = nbyte
    for i in range(n):
        f = open(nome + str(i) + extension, "wb")
        print("[INFO]: Creation of: " + nome + str(i) + extension + " ("+str(nbyte)+" bytes) started!")
        while nbyte_temp > 0:
            if nbyte_temp > __max:
                f.write(os.urandom(__max))
                nbyte_temp -= __max
            else:
                f.write(os.urandom(nbyte))
                nbyte_temp = 0
        f.close()
        print("[SUCCESS]: Creation of: " + nome + str(i) + extension + " completed!")
        nbyte_temp = nbyte