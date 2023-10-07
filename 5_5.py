###UTF-8###
from collections import Counter


def transform_to_set(input_list):
    new_list =[]
    c = Counter(input_list)
    b = c.most_common()

    for i in b:
        new_list.append(int(i[0]))
        t = 2
        for x in range(i[1]-1):
            new_list.append(str(i[0])*t)
            t+=1
    return new_list


list_1= [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]


print(f'{transform_to_set(list_1)}')
print(f'{transform_to_set(list_2)}')
print(f'{transform_to_set(list_3)}')

