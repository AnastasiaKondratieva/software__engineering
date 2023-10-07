###UTF-8###

numeric = int(input('Введи число от 0 до 10: '))
if isinstance(numeric, int) and 0 <= numeric <= 10:
    if 0 <= numeric <= 3:
        print('число в диапазоне 0 -> 3 включительно')
    if 3 < numeric < 6:
        print('число в диапазоне 3 -> 6')
    if 6 <= numeric <= 10:
        print('число в диапазоне от 6 -> 10 включительно ')
else:
    print('Вводимое число должно быть в диапазоне от 0 до 10')