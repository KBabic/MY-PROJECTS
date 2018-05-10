import random
import string

# for example week password has 5 random letters, lowercase
# medium password has 8 characters, first one is capitalized letter, others can be any alphanumeric characters
# strong pass has 12 random characters of any kind

while True:

    strength = input('How strong your password should be? Strong (s), medium (m) or weak (w)? ')
    password = ''
    alphabet = list(set(string.ascii_lowercase))
    nums = [0,1,2,3,4,5,6,7,8,9]
    others = ['+','-','*','/',':','!','?','_','%','$','#','@','^','&','=']

    if strength == 'w':
        counter = 0
        while counter < 5:
            shuffle(alphabet)
            password += alphabet.pop(0)
            counter += 1
        break

    elif strength == 'm':
        counter = 0
        shuffle(alphabet)
        password += alphabet.pop(0).upper()
        while counter < 7:
            rand_num = randint(0,1)
            if rand_num == 0:
                shuffle(nums)
                password += str(nums.pop(0))
                counter += 1
            else:
                shuffle(alphabet)
                password += alphabet.pop(0)
                counter += 1
        break

    elif strength == 's':
        counter = 0
        while counter < 12:
            rand_num = randint(0,2)
            if rand_num == 0:
                shuffle(nums)
                password += str(nums.pop(0))
                counter += 1
            elif rand_num == 1:
                shuffle(alphabet)
                password += alphabet.pop(0)
                counter += 1
            else:
                shuffle(others)
                password += others.pop(0)
        break
    else:
        print('Guess you did not type in a valid letter for password strength. Please try again!')

print('Your password is: ', password) 
