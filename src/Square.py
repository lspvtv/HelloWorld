from src.Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_a):
        super().__init__(side_a, side_a)
        self.side_a = side_a
        self.name = 'Square'
