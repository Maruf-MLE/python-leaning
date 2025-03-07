class student:
    roll=''
    gpa=''
    def __init__(self,a,b):
        self.roll=a
        self.gpa=b
    
    def pr(self):
        print(f' roll:{self.roll} or gpa:{self.gpa}')
maruf=student(125,3.96)
maruf.pr()
anisul=student(102,3.95)
anisul.pr()
harry=student(103,3.95)
harry.pr()
