while True:
    try:
        a = int(input('Please type the first number: '))
        break
    except:
        print("Looks like you didn't enter a number. Try again. ")

while True:
    try:
        b = int(input('Please type the second number: '))
        break
    except:
        print("Looks like you didn't enter a number. Try again. ")    

def calc(a, b, op):
    
    if op == '+':
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a + b))
    elif op == '-':
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a - b))
    elif op == '*':
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a * b))
    elif op == '/':
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(round((a / b),4)))

while True:
    
    op = input('What kind of operation would you like to do?\nChoose between "+, -, *, /" : ')
    if op not in ['+','-','*','/']:
        print('Please only type one of these characters: "+, -, *, /"!')
    else:
        print(calc(a, b, op))
        break