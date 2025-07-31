import random
 
a = random.randint(1,100)

b= -1
guesses=0
while(b != a):

    b = int(input("Enter a number : "))
    guesses+=1


    if(b>a):

        print("LOwer number")
    
    else:
        print("Higher number")


print(f"You have guessed right in {guesses} attempt")