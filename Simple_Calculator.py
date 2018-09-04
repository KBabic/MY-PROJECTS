def input_nums(orderedNum):
    while True:
        try:
            return int(input('Please type the {} number: '.format(orderedNum)))
            break
        except:
            print("Looks like you didn't enter a number. Try again. ")

a = input_nums('first')
b = input_nums('second')

operations = { '+': a+b, '-': a-b, '*': a*b, '/': round((a / b),4)}

def calc(a, b, op):
    return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(operations[op])

while True:

    op = input('What kind of operation would you like to do?\nChoose between "+, -, *, /" : ')
    if op not in operations.keys():
        print('Please only type one of these characters: "+, -, *, /"!')
    else:
        print(calc(a, b, op))
        break
