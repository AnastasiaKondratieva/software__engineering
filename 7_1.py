###UTF-8###
import re
from collections import Counter

def count_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()  # Чтение файла и приведение к нижнему регистру

        # Используем регулярное выражение для извлечения слов из текста
        words = re.findall(r'\b\w+\b', text)
        print(words)

        # Подсчет частоты встречаемости слов
        word_counts = Counter(words)

        # Находим самое часто встречающееся слово
        most_common_word, count = word_counts.most_common(1)[0]

        # Вывод результата
        print(f"Количество слов в файле: {len(words)}")
        print(f"Самое часто встречающееся слово: '{most_common_word}' (встречается {count} раз)")

# Укажи путь к своему текстовому файлу
file_path = 'text.txt'
count_words(file_path)

