f = open("poems.txt")
data = f.read()
if("twinkle" in  data):
    print("twinkle is present")
f.close