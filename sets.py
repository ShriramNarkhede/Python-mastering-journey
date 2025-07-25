Months = {"January","February", "March", "April", "May", "June"} 
days=set(["mon","tue","wed","thu","fri","sat","sun"])
print("\nRemoving some months from the set...")
Months.discard("January")

print(Months)
days.remove("mon")
print(days)
for i in Months:
    print(i)

Months.all()