###UTF-8###

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

def calculate_triangle_area(a, b, c):
    # Полупериметр треугольника
    s = (a + b + c) / 2
    # Вычисление площади треугольника по формуле Герона
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

small_triangle = calculate_triangle_area(min(one), min(two), min(three))

big_triangle = calculate_triangle_area(max(one), max(two), max(three))

print(small_triangle)
print(big_triangle)