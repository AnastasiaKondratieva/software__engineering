###UTF-8###

class SmartLamp():
    def __init__(self, model, color):
        self.model = model
        self.color = color
        self._brithness = 0
        self.__state = "off"

    def power_on(self):
        self.__state = 'On'
        self._brithness = 100
        print(f'Мое состояние: {self.__state} \n'
              f'Яркость: {self._brithness}')

    def info(self):
        print(f'Я светильник {self.model}\n'
              f'Цвет: {self.color}\n'
              f'Состояние {self.__state}\n'
              f'Яркость: {self._brithness}')


my_lamp = SmartLamp('Тиронозавр', 'черный')
print(my_lamp._brithness) #вывод защищенного атрибута
# print(my_lamp.__state) #ошибка доступа к приватному атрибуту
print(my_lamp._brithness == 70) #ошибка доступа к внешнему изменению защищенного атрибута
my_lamp.power_on() #корректный доступ к изменению защищеного и приватного атрибута функией класса
