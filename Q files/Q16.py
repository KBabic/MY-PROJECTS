# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
ls = input('')
lst = list()
for char in ls.split(','):
    lst.append(int(char))
new_lst = [str(x**2) for x in lst if x%2!=0]
print(','.join(new_lst))

# another way:
# values = input()
# numbers = [x for x in values.split(",") if int(x)%2!=0]
# print ",".join(numbers)
