class programmer :
    company = "Microsoft"
    def __init__(self,name,salary,pin):
        self.name= name 
        self.salary=salary
        self.pin=pin

p = programmer("anuj",12000000,234567)
print(p.name,p.salary,p.pin,p.company)
r = programmer("rohan",12000000,234567)
print(r.company, r.name,r.salary,r.pin,)

 