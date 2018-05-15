# Define a generator which can iterate the numbers, which are divisible by 7, between a given range 1 and n.

n = input('Enter an integer: ')
def div_7(x):
    for i in range(int(x)+1):
        if i> 0 and i%7 == 0:
            yield i

for i in div_7(n):
    print(str(i))
