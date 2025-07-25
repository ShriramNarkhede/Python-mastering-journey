import random

r=random.randint(1,10)

i=0
chances=3
print("YOU HAVE ONLY 3 CHANCESS") 
while(i<3):
      chances=chances-1
      i=i+1
      print("Guess the number Between 1 to 10")
      userguess=int(input())
      if(r is userguess):
            print("*********Victory*********")
            print("You guessed Number is right ")
            break

      elif(chances == 0 ):
                  print("%%%%%%%%%%%%%%%%%%%%----GAME OVER----%%%%%%%%%%%%%%%%%%%%")
                  break
      
      else:
            if(r>userguess):
                  print("Your number is smaller ")
            else:
                  print("Your number is bigger ")
            print("\nTry again")
      print("Only ",chances," Chances Are Left ")           
            
      continue
            