a=int(input("enter 1st sub marks:"))
b=int(input("enter 1st sub marks:"))
c=int(input("enter 1st sub marks:"))

total_percentage=(a+b+c)*100/300
if(total_percentage>=40 and a>=33 and b>=33 and c>=33):
    print("congrats,you're passes",total_percentage)
else:
    print("Failed,try again next year",total_percentage)
      