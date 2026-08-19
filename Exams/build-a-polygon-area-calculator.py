class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, new_width) -> None:        
        if not isinstance(new_width, int):
            raise TypeError("Width must be a integer number")
        if new_width <= 0:
            raise ValueError("Must be a positive value")
        self.__width = new_width

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, new_height: int) -> None:        
        if not isinstance(new_height, (int)):
            raise TypeError("Width must be a number")
        if new_height <= 0:
            raise ValueError("Must be a positive value")
        self.__height = new_height

    def get_area(self)->int:
        return self.width * self.height
    
    def get_perimeter(self)->int:
        return 2*(self.width + self.height)
    
    def get_diagonal(self)-> int | float:
        return (self.width**2 + self.height**2)**(1/2)
    
    def get_picture(self)-> str:
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'        
        return ('*' * self.width + '\n') * self.height

    def get_amount_inside(self, shape) -> int:
        if not isinstance(shape, Rectangle):
            raise TypeError("Must be a Rectangle")                
        return (self.width // shape.width) * (self.height // shape.height)
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_width(self, side): # type: ignore
        self.width = side
        self.height = side

    def set_height(self, side):  # type: ignore
        self.width = side
        self.height = side

    def set_side(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return f'Square(side={self.width})'

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