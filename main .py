class Shape():
    def __int__(self):
        self.area=0

    def get_area(self):
        if self.area==0:
            self.acumulate_area()
        print (self.area)
        return self.area

class Ellipse(Shape):
    def __init__(self,a,b):
        self._a=a
        self._b=b
        self.area=0

    def acumulate_area(self):
        self.area=3.14*self._a*self._b
        print ('椭圆的面积')

class Square(Shape):
    def __init__(self,a):
        self._a=a
        self.area=0

    def acumulate_area(self):
        self.area=self._a*self._a
        print('正方形的面积')

class Rectangle(Shape):
    def __init__(self,a,b):
        self._a=a
        self._b=b
        self.area=0

    def acumulate_area(self):
        self.area=self._a*self._b
        print('矩形的面积')

class Circle(Shape):
    def __init__(self,a):
        self._a=a
        self.area=0

    def acumulate_area(self):
        self.area=3.14*self._a*self._a
        print('圆的面积')

shapes=[Ellipse(10,20),Square(15),Circle(5),Rectangle(20,15),Circle(5),Square(15),Ellipse(10,20)]


def computer_area(shapes):
    num=0
    for i in range(0,len(shapes)):
        num=num+shapes[i].get_area()
    return num

total_area=computer_area(shapes)
print('面积之和:',total_area)
