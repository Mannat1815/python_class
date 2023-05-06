class Rectangle:
    def __init__(self, l, b):
        self.length=l
        self.breadth=b     
    def getlength(self):
        return self.length
    def getbreadth(self):
        return self.breadth
    def setlength(self, length):
        self.length=length
    def setbreadth(self, breadth):
        self.breadth=breadth
    def __str__(self):
        return "length:"+str(self.length)+"\nbreadth:"+str(self.breadth)
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
R1= Rectangle(4,6)
R2= Rectangle(78,67)
print(R1)
print(R2)
print(R1.area())
print(R1.perimeter())
print(R2.area())
print(R2.perimeter())

