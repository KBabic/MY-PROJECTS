import json
f = open('C:\\Users\\Kaja\\Desktop\\MY-PROJECTS\\birthdays.json')
birthdays = json.load(f)
f.close()

months = []
count_month = []

for key in birthdays:
    months.append(birthdays[key][0:2])

for month in set(months):
    month_count = months.count(month)
    if month_count != 1:
        print('Several persons were born in {}. month:'.format(month))
        for key in birthdays:
            if birthdays[key][0:2] == month:
                print(key)
    else:
        continue

    
