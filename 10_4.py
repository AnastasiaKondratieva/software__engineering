###UTF-8###

# декоратор умноженя результата функции на 2
def multiply_by_two(func):
    def wrapper(*args, **kwargs):  # функция умножает результат оригинальной функции на два.
        result = func(*args, **kwargs)
        return result * 2

    return wrapper


@multiply_by_two
def add_two_numbers(a, b):  # принимает два числа и возвращает их сумму.
    return a + b


@multiply_by_two
def concatenate_strings(str1, str2):  # принимает две строки и возвращает их сумму.
    return str1 + str2


# Тесты
result1 = add_two_numbers(3, 5)
result2 = concatenate_strings("Hello", " World!")

# Вывод результата в консоль
print("Результат сложения, умноженный на два:", result1)
print("Результат конкатенации, умноженный на два:", result2)
