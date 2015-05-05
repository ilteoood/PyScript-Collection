__author__ = "iLTeoooD"
import os

name = os.path.realpath(__file__)
curpath, name = os.path.split(name)


def ricorsiva(path, depth=0):
    for x in os.listdir(path):
        x=path+os.sep+x
        if os.path.isdir(x):
            for i in range(0, depth):
                f.write("\t")
            f.write(x.split(os.sep)[-1] + "\n")
            ricorsiva(x, depth + 1)

if os.path.isfile("list.txt"):
    f = open("list.txt", "r")
    nPrec = 0
    for x in f.read().split("\n"):
        x=x.split("\t")
        nAtt=len(x)
        if nAtt < nPrec:
            for i in range(0, nPrec - nAtt + 1):
                curpath, name = os.path.split(curpath)
        elif nAtt == nPrec:
            curpath, name = os.path.split(curpath)
        curpath+=os.sep+x[-1]
        nPrec = nAtt
        try:
            os.mkdir(curpath)
        except FileExistsError:
            pass
    f.close()
else:
    print("No \"list.txt\" found.")
