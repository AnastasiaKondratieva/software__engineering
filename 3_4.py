###UTF-8###

sentence = input("Введите предложение на английском: ")

print(f"Длина предложения: {len(sentence)} символов")

sentence_lower = sentence.lower()
print(f"Предложение в нижнем регистре: {sentence_lower}")

vowels = ['a','e','i','o','u']
vowel_count = sum(sentence_lower.count(vowel) for vowel in vowels)
print(f"Количество гласных: {vowel_count}")

sentence_beauty = sentence_lower.replace("ugly", "beauty")
print(f"Предложение с заменой 'ugly' на 'beauty': {sentence_beauty}")

if sentence_lower.startswith("the") and sentence_lower.endswith("end"):
    print("Предложение начинается с 'The' и заканчивается на 'end'")
else:
    print("Предложение не начинается с 'The' и не заканчивается на 'end'")
