from random import randint 

class train :
    def __init__(self,trainNo):
        self.trainNo= trainNo
    def book(self,fro,to):
        print(f"Ticket is booked in train no : {self.trainNo} from {fro} to {to}")

    def getstatus(self):
      print(f"train no : {self.trainNo} is running on time")

    def getfare(self, trainNo,fro,to):
        print(f"ticket fare in train no : {self.trainNo} from {fro} to {to} is {randit(222,800)}")

t = train (12298)
t.book("rampur","delhi")
