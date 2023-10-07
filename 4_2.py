###UTF-8###

import random

def roll_dice():
    # Бросаем игральную кость
    dice_value = random.randint(1, 6)
    print(f"Вы бросили кубик и выпало: {dice_value}")

    if dice_value in [5, 6]:
        print("Вы победили")
        return
    elif dice_value in [3, 4]:
        print("Вы продолжаете игру...")
        roll_dice()  # Рекурсивный вызов функции для броска кубика
    else:
        print("Вы проиграли")
        return
if __name__ == "__main__":
    roll_dice()  # Точка входа в программу
