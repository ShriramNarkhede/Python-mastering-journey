try:
      fh = open("testfile", "r")
      fh.write("This is my test file for exception handling!!")
except ValueError:
      print ("Error: can\'t find file or read data")
else:
      print ("Written content in the file successfully")
      fh.close()

try:
    c =9.9
    while True:
            c=c**3.8
            print(c,"\n")
except OverflowError as a:
    print(a)