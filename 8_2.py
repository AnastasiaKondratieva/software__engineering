###UTF-8###

class SmartLamp():
    def __init__(self, model, color):
        self.model = model
        self.color = color
        self.brithness = 0
        self.state = "off"

    def power_on(self):
        self.state = 'On'
        self.brithness = 100
        print(f'Мое состояние: {self.state} \n'
              f'Яркость: {self.brithness}')

    def info(self):
        print(f'Я светильник {self.model}\n'
              f'Цвет: {self.color}\n'
              f'Состояние {self.state}\n'
              f'Яркость: {self.brithness}')


my_lamp = SmartLamp('Тиронозавр', 'черный')
my_lamp.info()
print()
my_lamp.power_on()