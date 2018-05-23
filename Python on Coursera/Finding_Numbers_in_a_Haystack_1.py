import re
file = open('C:\\Users\\Kaja\\Desktop\\PYTHON COURSERA\\regex_sum_97957.txt')
content = file.readlines()
file.close()
num_sum = 0

for line in content:
    nums = re.findall('[0-9]+',line)
    int_nums = [int(x) for x in nums]
    num_sum += sum(int_nums)

print(num_sum)
