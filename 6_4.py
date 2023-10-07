###UTF-8###

def extract_subtuple(data, element):
    start_index = None
    end_index = None

    for i, item in enumerate(data):
        if item == element:
            if start_index is None:
                start_index = i
            end_index = i

    if start_index is None:
        return tuple()
    elif start_index == end_index:
        return data[start_index:]
    else:
        return data[start_index:end_index]

# Примеры использования:
tuple1 = (1, 2, 3)
element1 = 8
result1 = extract_subtuple(tuple1, element1)
print(result1)  # Вывод: ()

tuple2 = (1, 8, 3, 4, 8, 8, 9, 2)
element2 = 8
result2 = extract_subtuple(tuple2, element2)
print(result2)  # Вывод: (8, 3, 4, 8)

tuple3 = (1, 2, 8, 5, 1, 2, 9)
element3 = 8
result3 = extract_subtuple(tuple3, element3)
print(result3)  # Вывод: (8, 5, 1, 2, 9)
