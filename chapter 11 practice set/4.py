class ComplexNumber :
    def __init__(self,i,r):
        self.i=i
        self.r=r

    def __add__(self,c2):
        return ComplexNumber(self.i+c2.i,self.r+c2.r)
    
    def __str__(self):
        return f"{self.r}+{self.i}i"
    

c1= ComplexNumber(1,2)
c2= ComplexNumber(3,4)
print(c1+c2)
