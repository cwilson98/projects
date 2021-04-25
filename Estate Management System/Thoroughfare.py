from Estate import Estate

class Thoroughfare:

    def __init__(self, name: str) -> None:
        self.name = name
        self.properties = []

    def __repr__(self):
        return f'Thoroughfare(name={self.name}'