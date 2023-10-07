###UTF-8###
from collections import Counter

def string_conversion(i_str):
    number_list = []
    number_dict_1 = {}
    for number in i_str:
        number_list.append(number)
    number_dict = Counter(number_list).most_common(3)
    for x in number_dict:
        print([x[0], x[1]])
        number_dict_1.update({f"{int(x[0])}": f"{int(x[1])}"})
    sorted_dict = dict(sorted(number_dict_1.items(), key=lambda x: x[0]))
    return print(sorted_dict)


input_str=input('3478574576435630295')
string_conversion(input_str)

