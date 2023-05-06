class Student :
    def __init__(self):
         self.marklist=[]
         self.percentage=0
         self.grade=[]
         self.division=[]
    def setMarks(self):
        for i in range(5):
            marks= int(input("Enter marks for subject"))
            self.marklist.append(marks)
    def percentagecalculate(self):
        self.percentage=(sum(self.marklist)/5)*100
        return self.percentage
    def gradecalculate(self):
        for marks in self.marklist:
            if marks>=90:
                self.grade.append("A")
            elif marks<90 and marks>=80:
                self.grade.append("B")
            elif marks<80 and marks>=65:
                self.grade.append("C")
            elif marks<65 and marks>=40:
                self.grade.append("D")
            else:
                self.grade.append("E")
        return self.grade
    def divisioncalculate(self):
        for marks in self.marklist:
            if marks >=60:
                self.division.append("I")
            elif marks<60 and marks>=50:
                self.division.append("II")
            elif marks<50 and marks>=35:
                self.division.append("III")
        return self.division
    def __str__(self):
        return "marks:"+str(self.marklist)+"\npercentage:"+str(self.percentage)+"\ngrade:"+str(self.grade)+"\ndivision:"+str(self.division)

S1=Student()
S1.setMarks()
S1.percentagecalculate()
S1.gradecalculate()
S1.divisioncalculate()
print(S1)
