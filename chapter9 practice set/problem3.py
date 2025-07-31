word = "donkey"

with open("abhay.txt","r") as f:
    content= f.read()

contentNew= content.replace(word,"######")

with open("abhay.txt", "w") as f:
    f.write(contentNew)
   