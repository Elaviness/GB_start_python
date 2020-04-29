""" Создать класс TrafficLight (светофор) и определить у него 
один атрибут color (цвет) и метод running (запуск). Атрибут 
реализовать как приватный. В рамках метода реализовать переключение 
светофора в режимы: красный, желтый, зеленый. Продолжительность 
первого состояния (красный) составляет 7 секунд, 
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше 
усмотрение. Переключение между режимами должно осуществляться 
только в указанном порядке (красный, желтый, зеленый). 
Проверить работу примера, создав экземпляр и вызвав описанный метод."""
from time import sleep

class TrafficLight:
    def __init__ (self):
        TrafficLight.color = 'Red'

    def running(self):
        while True:
            if self.color == 'Red':
                print(self.color)
                sleep(7)
                self.color = 'Yellow'
            elif self.color == 'Yellow':
                print(self.color)
                sleep(2)
                self.color = 'Green'
            elif self.color == 'Green':
                print(self.color)
                sleep(10)
                self.color = 'Red'

my_light = TrafficLight()
my_light.running()
