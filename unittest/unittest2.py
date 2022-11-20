import unittest

#from square import Square

class Square:
    def __init__(self, length) -> None:
        self.length = length

    def area(self):
        return self.length * self.length

class TestSquare(unittest.TestCase):
    def test_area(self):
        square = Square(10)
        area = square.area()
        self.assertEqual(area, 100)