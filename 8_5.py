###UTF-8###

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Гав-гав!"

class Cat(Animal):
    def speak(self):
        return "Мур-мур"

animals = [Dog("Бобик"), Cat("Мурка"), Dog("Жуля")]

for animal in animals:
    print(f'{animal.name}: {animal.speak()}')
