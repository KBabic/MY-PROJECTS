def gen_fib(n):
   
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b

while True:        
    try:
        num = int(input('Up to which number would you like to see Fibonacci sequence?\nPlease enter an integer: '))
        print([x for x in list(gen_fib(num)) if x <= num])
        break
    except:
        print('\nPlease enter an integer!\n')