import json
birthdays = {'Russell Crowe':'04/07/1964', 'Christian Bale':'01/30/1974','Hugh Jackman':'10/12/1968','Jennifer Connelly': '12/12/1970',
'Charlize Theron':'08/07/1975', 'Kristen Stewart':'04/09/1990', 'Alec Baldwin':'04/03/1958', 'Lena Headey':'12/26/1973'}
f1 = open('birthdays.json','w')
json.dump(birthdays, f1)
f1.close()
f2 = open('birthdays.json','r')
birth_dict = json.load(f2)
f2.close()

print('I know birthdays of some celebrities: ')
for key in birth_dict:
    print(key)
print('\n')
name = input('Who\'s birthday would you like to know?')
if name in birth_dict.keys():
    print('{}\'s birthday is {}'.format(name, birth_dict[name]))
else:
    print('Sorry, I don\'t know that persons\'s birthday.')
