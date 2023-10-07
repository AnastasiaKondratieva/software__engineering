###UTF-8###

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            if not data:
                raise Exception("Файл пустой")
            else:
                print(f"Информация из файла:\n{data}")
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден")
    except Exception as e:
        print(f"Ошибка: {e}")

# Создание пустого файла
with open("empty_file.txt", "w") as empty_file:
    pass

# Создание файла с информацией
with open("non_empty_file.txt", "w") as non_empty_file:
    non_empty_file.write("Здесь есть какая-то информация")

# Попытка считывания из пустого файла
read_file("empty_file.txt")

# Попытка считывания из непустого файла
read_file("non_empty_file.txt")
