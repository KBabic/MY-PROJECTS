# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# At least 1 letter between [a-z]
# At least 1 number between [0-9]
# At least 1 letter between [A-Z]
# At least 1 character from [$#@]
# Minimum length of transaction password: 6
# Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria.
# Passwords that match the criteria are to be printed, each separated by a comma.

import re
passwords = input('Enter passwords for check: ')
ls = list()
for password in passwords.split(','):
    if 6 <= len(password) <= 12 and len(re.findall('[a-z]+',password)) >= 1 and len(re.findall('[0-9]+',password)) >= 1 and len(re.findall('[A-Z]+',password)) >= 1 and len(re.findall('[$#@]+',password)) >= 1:
            ls.append(password)
print('Entered passwords:',passwords)
print('Correct passwords:',','.join(ls))

   
