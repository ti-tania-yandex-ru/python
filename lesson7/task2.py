from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def consumption(self):
        print('Считаем расход ткани: ')


class Coat(Clothes):

    @property
    def consumption(self):
        return self.size / 6.5 + 0.5


class Costume(Clothes):

    @property
    def consumption(self):
        return self.size * 2 + 0.3


coat1 = Coat(48)
coat2 = Coat(54)
costume1 = Costume(1.64)
costume2 = Costume(1.70)
total_consumption = coat1.consumption + coat2.consumption + costume1.consumption + costume2.consumption
print(f'Расход на пошив одежды: {total_consumption} кв м.')
