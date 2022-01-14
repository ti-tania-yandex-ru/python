class Worker:

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


person1_income = {"wage": 1000, "bonus": 100}
person2_income = {"wage": 700, "bonus": 70}
position1 = Position('John', 'Doe', 'Senior Specialist', person1_income)
position2 = Position('Mark', 'Ruffalo', 'Middle Specialist', person2_income)
print(f'Person1 fullname: {position1.get_full_name()}')
print(f'Person1 total income: {position1.get_total_income()}')
print(f'Person2 fullname: {position2.get_full_name()}')
print(f'Person2 total income: {position2.get_total_income()}')
