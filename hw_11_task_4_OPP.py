class Table:

    def __init__(self, width, length, height):
        self.__width = width
        self.__length = length
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, new_width):
        self.__width = new_width

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, new_length):
        self.__length = new_length

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height):
        self.__height = new_height

    def area(self):
        return self.__width * self.__length

    def capacity(self):
        s = self.__width * self.__length
        if s <= 4:
            return 'Вместимость стола до 4 человек.'
        else:
            return 'Сядет более 4 человек'


table = Table(1, 1.5, 0.7)

print(table.width)
print(table.length)
print(table.height)

print(table.area())
print(table.capacity())

table.width = 2
table.length = 2.5
print(table.width)
print(table.length)
print(table.area())
print(table.capacity())
