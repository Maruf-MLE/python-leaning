class student:
    roll=''
    gpa=''
    def set_value(self,a,b):
        self.roll=a
        self.gpa=b
        
    def pr(self):
        print(f' roll:{self.roll} or gpa:{self.gpa}')
maruf=student()
maruf.set_value(125,3.96)
maruf.pr()

anisul=student()
anisul.set_value(102,3.95)
anisul.pr()

harry=student()
harry.set_value(103,3.95)
harry.pr()
