###UTF-8###

def fib_with_saving_to_file(n):
    a, b = 1, 1
    with open("fib.txt", "w") as file:  # используем with open("fib.txt", "w") as file для открытия файла в режиме записи.
        for _ in range(n):              # В цикле for мы записываем текущее число в файл и затем возвращаем его с помощью yield.
            file.write(str(a) + "\n")
            yield a
            a, b = b, a + b

# Генерация чисел Фибоначчи и сохранение их в файл
fibonacci_sequence = list(fib_with_saving_to_file(200))

# Вывод последнего числа Фибоначчи в консоль
print(f"Число Фибоначчи под номером 200: {fibonacci_sequence[-1]}")


