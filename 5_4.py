###UTF-8###


one = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
two = [4,2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
three = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

def correction_of_grades(list_of_ratings):
    while 2 in list_of_ratings:
        list_of_ratings.remove(2)

    for i in range(len(list_of_ratings)):
        if list_of_ratings[i] == 3:
            list_of_ratings[i] = 4
    return list_of_ratings

print(correction_of_grades(one))
print(correction_of_grades(two))
print(correction_of_grades(three))