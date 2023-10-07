###UTF-8###

# Создание собственного исключения
class CustomError(Exception):
    pass

# Фрагмент 1: Бросаем исключение, если число отрицательное
def check_positive_number(number):  #Функция проверяет, является ли число отрицательным, и, если да, бросает исключение CustomError.
    if number < 0:
        raise CustomError("Число не может быть отрицательным")

# Фрагмент 2: Ловим и обрабатываем исключение
try:
    user_input = int(input("Введите число: "))
    check_positive_number(user_input) #Если число отрицательное, бросается исключение CustomError, которое мы ловим и выводим соответствующее сообщение.
    print("Введенное число положительное.")
except CustomError as ce:
    print(f"Ошибка: {ce}")
except ValueError:
    print("Ошибка: Введите целое число.")
