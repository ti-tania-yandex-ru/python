class Cage:
    def __init__(self, cells_amount):
        self.cells_amount = cells_amount

    def __add__(self, other):
        return Cage(self.cells_amount + other.cells_amount)

    def __sub__(self, other):
        result = self.cells_amount - other.cells_amount
        if result >= 0:
            return Cage(result)
        else:
            print('Вторая клетка крупнее первой. ')
            return Cage(0)

    def __mul__(self, other):
        return Cage(self.cells_amount * other.cells_amount)

    def __truediv__(self, other):
        return Cage(self.cells_amount // other.cells_amount)

    def make_order(self, cells_in_row):
        row_count = self.cells_amount // cells_in_row
        rest = self.cells_amount % cells_in_row
        return ("*" * cells_in_row + "\n") * row_count + "*" * rest


cage1 = Cage(18)
print(cage1.make_order(7))
cage2 = Cage(7)
cage3 = cage1 + cage2
print(cage3.cells_amount)
print(cage3.make_order(10))
cage4 = cage1 - cage2
print(cage4.cells_amount)
print(cage4.make_order(4))
cage5 = cage1 * cage2
print(cage5.cells_amount)
print(cage5.make_order(25))
cage6 = cage1 / cage2
print(cage6.cells_amount)
print(cage6.make_order(3))
cage7 = cage6-cage1
print(cage7.cells_amount)
print(cage7.make_order(3))
