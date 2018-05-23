import re
file = open('C:\\Users\\Kaja\\Desktop\\PYTHON COURSERA\\regex_sum_97957.txt')
print(sum([int(x) for x in re.findall('[0-9]+', file.read())]))
file.close()
