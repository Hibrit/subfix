from os import remove, listdir, getcwd, sep
from os.path import isfile, join

mypath = getcwd()
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
files.remove("fixer.py")
files.remove("cleaner.py")

for i in files:
    try:
        remove(i)
    except:
        print("wut")
        input()


_files = [
    f
    for f in listdir(mypath + sep + "fixed")
    if isfile(join(mypath + sep + "fixed", f))
]

for i in _files:
    path = mypath + sep + "fixed" + sep + i
    try:
        remove(path)
    except:
        print("wut")
        input()
