class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Автомобиль {self.name} поехал.')

    def stop(self):
        print(f'Автомобиль {self.name} остановился.')

    def turn(self, direction):
        print(f'Автомобиль {self.name} повернул {direction}.')

    def show_speed(self):
        print(f'Скорость автомобиля {self.name} равна {self.speed}')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Превышение допустимого значения скорости по городу 60 км/ч!')


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Превышение допустимого значения скорости рабочего авто 40 км/ч!')


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


town_car1 = TownCar(65, 'white', 'Mazda', False)
town_car2 = TownCar(59, 'green', 'Skoda', False)
work_car1 = WorkCar(45, 'red', 'Tractor', False)
sport_car1 = SportCar(90, 'red', 'Lamborgini', False)
police_car1 = PoliceCar(70, 'white', 'Land Rover')

town_car1.go()
town_car1.show_speed()
town_car1.turn('Направо')
town_car1.stop()

town_car2.go()
town_car2.show_speed()
town_car2.turn('Налево')
town_car2.stop()

work_car1.go()
work_car1.show_speed()
work_car1.turn('Направо')
work_car1.stop()

sport_car1.go()
sport_car1.show_speed()
sport_car1.turn('Направо')
sport_car1.stop()

police_car1.go()
police_car1.show_speed()
police_car1.turn('Направо')
police_car1.stop()
