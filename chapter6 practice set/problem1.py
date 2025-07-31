a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=int(input("enter the number:"))
d=int(input("enter the number:"))
if(a>b and a>c and a>d):
    print("a is greatest")
if(b>a and b>c and b>d):
    print("b is greatest")
if(c>b and c>a and a>d):
    print("c is greatest")
if(d>b and d>c and d>a):
    print("d is greatest")