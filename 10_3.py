###UTF-8###

def add_two_numbers():
    try:
        user_input = input("Введите число: ")
        number = float(user_input)
        result = 2 + number
        print(f"Результат сложения: {result}")
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число.")

# Тесты
add_two_numbers()
add_two_numbers()
add_two_numbers()
