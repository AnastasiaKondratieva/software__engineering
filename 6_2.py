###UTF-8###

def remove_first_occurrence(tup, element):
    if element in tup:
        index = tup.index(element)
        return tup[:index] + tup[index + 1:]
    else:
        return tup


tuple1 = (1, 2, 3)
element1 = 1
result1 = remove_first_occurrence(tuple1, element1)
print(result1)

tuple2 = (1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2)
element2 = 3
result2 = remove_first_occurrence(tuple2, element2)
print(result2)

tuple3 = (2, 4, 6, 6, 4, 2)
element3 = 9
result3 = remove_first_occurrence(tuple3, element3)
print(result3)