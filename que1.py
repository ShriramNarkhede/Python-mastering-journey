f=open("abc.txt","r")
cont=f.read()

#f1=open=("pqr.txt","w")
print(cont)
f.close()

f1=open("pqr.txt","+a")
f1.write(cont)
f1.close()