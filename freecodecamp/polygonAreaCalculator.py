
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    def set_width(self,width):
        self.width = width
    
    def set_height(self,height):
        self.height = height

    def get_area(self):
        return self.height * self.width
    
    def get_perimeter(self):
        return 2*(self.height + self.width)
    
    def get_diagonal(self):
        return ((self.width**2 + self.height**2) ** 0.5)
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        
        return (('*'*self.width) + '\n')*self.height
    
    def get_amount_inside(self,shape):
        area_of_rect = self.get_area()
        area_of_shape = shape.get_area()

        return area_of_rect // area_of_shape
    
    def __str__(self):
        return f'{self.__class__.__name__}(width={self.width}, height={self.height})'

    

class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)
    
    def set_side(self,side):
        self.height = side
        self.width = side
    
    def set_width(self,width):
        self.set_side(width)
    
    def set_height(self,height):
        self.set_side(height)
    
    def __str__(self):
        return f'{self.__class__.__name__}(side={self.height})'


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))



"""
Output of the code
50
26
Rectangle(width=10, height=3)
**********
**********
**********

81
5.656854249492381
Square(side=4)
****
****
****
****

8
"""
