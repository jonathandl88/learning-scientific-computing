class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        output_string = ''
        for i in range(self.height):
            output_string += self.width * '*' + '\n'
        return output_string

    def get_amount_inside(self, other):
        # if type(self) != type(other) and (not isinstance(other, Square)):
        # return NotImplemented
        return self.get_area() // other.get_area()

    def __str__(self):
        arg_list = [f'{key}={val}' for key, val in vars(self).items()]
        args = ', '.join(arg_list)
        return str(f'{self.__class__.__name__}({args})')


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.height = height
        self.weidht = height

    def set_side(self, side):
        self.__init__(side)

    def __str__(self):
        return str(f'{self.__class__.__name__}(side={self.height})')


if __name__ == '__main__':
    r1 = Rectangle(4, 8)
    r2 = Rectangle(4, 4)
    r1.set_width(5)
    print(r1.get_picture())
    print(r1.get_amount_inside(r2))
    print(r1)
    s1 = Square(4)
    print(s1)
    s1.set_width(5)
    print(s1)
    s1.set_height(6)
    print(s1)
    s1.set_side(8)
    print(s1)