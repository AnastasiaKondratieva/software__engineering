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

    def power_off(self):
        self.state = 'Off'
        self.brithness = 0
        print(f'Мое состояние: {self.state} \n'
              f'Яркость: {self.brithness}')

    def info(self):
        print(f'Я светильник {self.model}\n'
              f'Цвет: {self.color}\n'
              f'Состояние {self.state}\n'
              f'Яркость: {self.brithness}')


# my_lamp = SmartLamp('Тиронозавр', 'черный')
# my_lamp.info()
# print()
# my_lamp.power_on()

class SmartLampV2(SmartLamp):
    def __init__(self, model, color, wifi_ssid, wifi_pass):
        super().__init__(model, color)
        self.ssid = wifi_ssid
        self.passwd = wifi_pass

    def wifi_connect(self):
        if self.ssid is not None and self.passwd is not None:
            return print(f'светильник подключен к cети {self.ssid} c паролем {self.passwd}')
        print('Укажи имя и пароль сети')



my_new_lamp = SmartLampV2('Диплодок', 'Розовый', 'home', 'Fn2jfk')
my_new_lamp.info()
print()
my_new_lamp.power_on()
print()
my_new_lamp.wifi_connect()
