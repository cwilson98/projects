from clothing_size import ClothingSize

class Clothing:

    def __init__(self, colour:str, material:str, size:ClothingSize):
        self.colour = colour
        self.material = material
        self.size = size

    def __repr__(self) -> str:
        return f'clothing(colour={self.colour}, material={self.material}, size={self.size})'

    def __str__(self) -> str:
        return f'This {self.material} is {self.colour} and is {self.size}'