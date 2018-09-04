my_list = []

length = int(input('How many elements will your list have? '))
print('\n')

while length > 0:
    element = int(input('Add a number to your list: '))
    length -= 1
    my_list.append(element)

print('\nYour list is:',my_list)

new_list = []

while len(my_list) > 0:

    for counter in range(1,len(my_list)):

        n = len(my_list)
        a = my_list[n-counter]
        b = my_list[n-counter-1]

        if a<b:
            my_list.remove(b)
            my_list.insert(n-counter,b)
        else:
            pass

    x = my_list.pop(0)
    new_list.append(x)

print('\nYour bubble sorted list is:',new_list)
