class a:
    def display(self):
        print('i am a a class')

class b:
    def display(self):
        
        print('i am a b class')

class c(b,a):
    pass
    # def display(self):

        # print('i am a c class')

x=c()
x.display()
