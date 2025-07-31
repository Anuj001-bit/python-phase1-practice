import random

'''
0 = Stone 
1 = paper
2 = scissor
'''

youstr=input("Enter your choice :")
youDict = {"s":0,"p":1,"sc":2}
reverseDict={0:"stone",1:"paper",2:"scissor"}
you = youDict[youstr]

computer = random.choice([0,1,2])
print(f"computer choose {reverseDict[computer]}\n You choose {reverseDict[you]}")

if(computer==you):
    print("It is a draw!")
else:
    if(computer==0 and you==1):
        print("You Win!")
    elif(computer==0 and you==2):
        print("you lost!")
    elif(computer==1 and you==0):
        print("you lost!")
    elif(computer==1 and you==2):
        print("you Win!")
    elif(computer==2 and you==0):
        print("you Win!")
    elif(computer==2 and you==1):
        print("you lost!")
    else:
        print("Something went wrong!")


