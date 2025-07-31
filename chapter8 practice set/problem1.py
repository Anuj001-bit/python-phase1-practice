def great():
    a= int(input("Enter a number:"))
    b = int(input("Enter a number:"))
    c= int(input("Enter a number:"))

    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
    
print("The greatest number is", great())
