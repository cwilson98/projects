from ClothingSize import ClothingSize

class Clothing:

    def __init__(self, colour:str, material:str, size:ClothingSize) -> None:
        self.__colour = colour
        self.__material = material
        self.__size = size

    def __repr__(self):
        return f'Clothing(colour={self.__colour}, material={self.__material}, size={self.__size})'

    def __str__(self):
        return f'The shirt is {self.__colour} made out of {self.__material} size {self.__size}'