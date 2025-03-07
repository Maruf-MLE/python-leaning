from abc import ABC,abstractclassmethod 
class shape(ABC):
    @abstractclassmethod
    def __init__(self,dim1,dim2):
        self.dim1=dim1
        self.dim2=dim2
    
    def area(self):
        pass

class triangle(shape):
    def area(self):
        area=0.5*self.dim1*self.dim2
        print(f'the tringle area is {area}')

class reactangle(shape):
    def area(self):
        area=self.dim1*self.dim2
        print(f'the reactangle area is {area}')


z=shape(20,30)

x=triangle(20,30)
x.area()
y=reactangle(20,30)
y.area()
        