def pattern(n):
    if(n==1):
        print("")
        return
    print ("*"*n)
    pattern(n-1)

pattern(5)