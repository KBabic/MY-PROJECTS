# You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers:
# 1: Sort based on name;
# 2: Then sort based on age;
# 3: Then sort by score.

import operator
ls = list()
while True:
    items = input('Enter name, age and height separated by comma: ')
    if not items:
        break
    else:
        my_tuple = tuple(items.split(','))
        ls.append(my_tuple)
sorted_ls = sorted(ls, key=operator.itemgetter(0,1,2))
for tup in sorted_ls:
    print(tup)
