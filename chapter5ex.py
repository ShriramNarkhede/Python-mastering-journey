import  turtle_graphics.packageex 
class stud:
#     studname=""
#     roll_no=0
#     seat_no=0
    def my5thsemsubjects(self,name,rolln,seatno):
        self.studname=name
        self.roll_no=rolln
        self.seat_no=seatno
        print(self.studname)
        print(self.roll_no)
        print(self.seat_no)
        print("PWP "," MAD ", " NIS ",end=" \n" )    
ob=stud()
# ob.my5thsemsubjects("shreeramnarkhede",39,331713)
ob.roll_no=69
print(ob.roll_no)
globalrollno=ob.roll_no
ob.my5thsemsubjects("shreeramnarkhede",globalrollno,331713)

