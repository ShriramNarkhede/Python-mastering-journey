"""r----> for  reading :::::default mode
w ----> for wirting
x=---->create file if not exist
a -----> for apppend 
t----->  text mod :::::::::default mode
b----->binary
R+------>read and write both """
f=open("fxxxfile.txt","a")
f.write("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
#f.write("ggggggggg")
# print(f.readline())
# f.seek(0)
# print(f.readline())
# list1=f.readline()
# print(list1)

# s1="THE NAME IS BOND JEMS BOND"
# vOfchars=f.write("fooook uu\n"+s1)
# print(vOfchars)

# f1=open("filetest2.txt","r")
# reading=f1.read()
# print(reading)


f.close()
# f1.close()