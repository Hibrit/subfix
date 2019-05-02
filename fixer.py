import re
from os import getcwd, listdir, sep
from os.path import isfile, join

mypath = getcwd()
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

files.remove("cleaner.py")
files.remove("fixer.py")

chr = "UTF-8"
for i in files:
    print(i)

for i in files:
    with open(i, "r", encoding=chr) as f:
        text = f.read()
        fixedtxt = ""
        for j in text:
            if j == "ð":
                fixedtxt += "ğ"
            elif j == "ý":
                fixedtxt += "ı"
            elif j == "þ":
                fixedtxt += "ş"
            elif j == "Ý":
                fixedtxt += "İ"
            elif j == "Þ":
                fixedtxt += "Ş"
            else:
                fixedtxt += j
        with open(mypath + sep + "fixed" + sep + i, "w", encoding=chr) as k:
            print(fixedtxt, file=k)
