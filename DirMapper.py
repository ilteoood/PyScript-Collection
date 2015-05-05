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


f = open("list.txt", "w")
ricorsiva(curpath)
f.close()
