"""  Реализовать класс Stationery (канцелярская принадлежность). 
Определить в нем атрибут title (название) и метод draw (отрисовка). 
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса 
Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов 
реализовать переопределение метода draw. Для каждого из классов 
методы должен выводить уникальное сообщение. Создать экземпляры 
классов и проверить, что выведет описанный метод для каждого экземпляра."""
class Stationary:
    def __init__(self, title= 'Any Tool'):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationary):
    def draw(self):
        self.title = 'Pen'
        print('Для рисования была выбрана ручка')


class Pencil(Stationary):
    def draw(self):
        self.title = 'pencil'
        print('Для рисования был выбран карандаш')


class Handle(Stationary):
    def draw(self):
        self.title = 'handle'
        print('Для рисования был выбран маркер')


pen = Pen()
pencil = Pencil()
handle = Handle()
pen.draw()
pencil.draw()
handle.draw()