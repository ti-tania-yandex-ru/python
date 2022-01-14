class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Рисуем ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Рисуем карандашом')


class Handle(Stationery):
    def draw(self):
        print('Рисуем маркером')


pen = Pen('Ручка')
pen.draw()
print(pen.title)

pencil = Pencil('Карандаш')
pencil.draw()
print(pencil.title)

handle = Handle('Маркер')
handle.draw()
print(handle.title)

stat = Stationery('Подручное средство')
stat.draw()
print(stat.title)
