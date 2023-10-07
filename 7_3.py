###UTF-8###
def analyze_text(file_path):
    # Инициализируем счетчики
    letter_count = 0
    word_count = 0
    line_count = 0

    # Открываем файл и читаем его построчно
    with open(file_path, 'r') as file:
        for line in file:
            # Увеличиваем счетчик строк
            line_count += 1
            # Увеличиваем счетчик букв на количество букв в текущей строке
            letter_count += len([char for char in line if char.isalpha()])
            # Увеличиваем счетчик слов на количество слов в текущей строке
            word_count += len(line.split())

    # Выводим результат
    print(f'Input file contains:')
    print(f'{letter_count} letters')
    print(f'{word_count} words')
    print(f'{line_count} lines')

# Вызываем функцию с указанием пути к файлу
analyze_text('input(7_3).txt')
