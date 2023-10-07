###UTF-8###

def replace_forbidden_words(sentence, forbidden_words):
    for word in forbidden_words:
        replacement = '*' * len(word)
        sentence = sentence.replace(word, replacement)
        sentence = sentence.replace(word.capitalize(), replacement)
        sentence = sentence.replace(word.upper(), replacement)
        sentence = sentence.replace(word.lower(), replacement)
    return sentence

def main():
    # Чтение запрещенных слов из файла
    with open('input(7_4).txt', 'r') as file:
        forbidden_words = file.read().split()
        print(forbidden_words)

    # Предложение для проверки
    sentence = "Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!!"

    # Замена запрещенных слов в предложении
    modified_sentence = replace_forbidden_words(sentence, forbidden_words)

    # Вывод результата
    print("Исходное предложение:")
    print(sentence)
    print("\nПредложение с замененными запрещенными словами:")
    print(modified_sentence)

if __name__ == "__main__":
    main()
