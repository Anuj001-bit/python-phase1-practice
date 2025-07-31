c1="Make a lot of money"
c2="buy now"
c3="click this"
message=str(input("enter your message"))
if(c1 in message or c2 in message or c3 in message):
    print("Spam")
else:
    print("genuine")