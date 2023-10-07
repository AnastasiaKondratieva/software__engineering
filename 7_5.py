###UTF-8###
# Открываем файл с числами для чтения
with open("numbers.txt", "r") as file:
    # Считываем числа и умножаем их на 2
    numbers = [int(x) * 2 for x in file.read().split()]

# Открываем файл для записи удвоенных чисел
with open("doubled_numbers.txt", "w") as output_file:
    # Записываем удвоенные числа в новый файл
    output_file.write(" ".join(map(str, numbers)))
