filewrite=open("fileiotesting.txt","a+")
list1=["eeee","dhfhfh","gdfh","yreury"]
filewrite.write("SHREERAMNARKHEDE \n")
filewrite.write("heyyy \n")
filewrite.write("heyyy shree\n")
filewrite.seek(0,0)
# filewrite.
print(filewrite.read())
# print(fileappend.readline())
# print(fileappend.name)
# print(fileappend.mode)
# print(fileappend.closed)

filewrite.close()
# print(fileappend.closed)

fread=open("fileiotesting.txt","r")
# listr=fread.readlines()
# print(fread.read(3))
fread.close()

import os
from pathlib import Path
# os.rename("XXX.txt","fio.txt")
#os.remove("tempCodeRunnerFile.py")
#rename folder
# print ("the dir is %s " %os.listdir(os.getcwd()))
# os.rename("folder1","folder2")


# os.rmdir("folder2")

print(os.path.exists("tempfolder"))
print(os.path.isdir("tempfolder"))
print(os.path.isfile("add.py"))