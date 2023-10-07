# user_interaction.py
from Tema_4 import calculate_triangle_area as calc


def get_user_input():
    # Запрашиваем длины сторон у пользователя
    a = float(input("Введите длину стороны a: "))
    b = float(input("Введите длину стороны b: "))
    c = float(input("Введите длину стороны c: "))
    return a, b, c


def main():
    print("Программа для вычисления площади треугольника по формуле Герона.")

    a, b, c = get_user_input()

    # Проверка на корректность длин сторон для построения треугольника
    if a + b > c and a + c > b and b + c > a:
        area = calc.calculate_triangle_area(a, b, c)
        print(f"Площадь треугольника: {area:.2f}")
    else:
        print("Треугольник с такими сторонами нельзя построить.")


if __name__ == "__main__":
    main()
