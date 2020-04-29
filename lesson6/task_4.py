""" Реализуйте базовый класс Car. У данного класса должны быть 
следующие атрибуты: speed, color, name, is_police (булево). 
А также методы: go, stop, turn(direction), которые должны сообщать, 
что машина поехала, остановилась, повернула (куда). Опишите 
несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. 
Добавьте в базовый класс метод show_speed, который должен 
показывать текущую скорость автомобиля. Для классов TownCar и 
WorkCar переопределите метод show_speed. При значении скорости 
свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о 
превышении скорости. """
class Car:
    def __init__(self, speed: int, color: str, name: str):
        self.speed = speed
        self.color = color
        self.name = name 
        self.is_police = False

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина по повернула на{direction}")
    
    def show_speed(self):
        print(f'Текущая скорость: {self.speed}')

class TownCar(Car):
    def show_speed(self):
        print(f'Текущая скорость: {self.speed}')
        if self.speed > 60:
            print('Скорость привышена')

class SportCar(Car):
    def show_speed(self):
        print(f'Текущая скорость: {self.speed}')
        if self.speed < 30:
            print('Реализуйте возможности вашего спорткара')

class WorkCar(Car):
    def show_speed(self):
        print(f'Текущая скорость: {self.speed}')
        if self.speed > 40:
            print('Скорость привышена')

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed,color,name)
        self.is_police = True

police = PoliceCar(45, 'белая', 'Skoda')
print(police.is_police)

town_car = TownCar(70, 'белая', 'Mazda')
town_car.show_speed()

work_car = WorkCar(45, 'черная', 'Opel')
work_car.show_speed()

sport_car = SportCar(25, 'красная', 'Ferarri')
sport_car.show_speed()
