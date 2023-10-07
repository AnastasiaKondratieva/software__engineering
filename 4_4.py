###UTF-8###

def average(*args):
    if not args:
        return 0
    return sum(args) / len(args)

if __name__ == "__main__":
    input_args = input("Введите числа через пробел: ").split()
    print(input_args)

    input_args = [int(item) for item in input_args]

    if input_args:
        avg = average(*input_args)
        print(f"Среднее арифметическое: {avg}")
