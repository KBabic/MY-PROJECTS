import json
f = open('C:\\Users\\Kaja\\Desktop\\MY-PROJECTS\\birthdays.json')
birthdays = json.load(f)
f.close()

months = []
count_month = []

for key in birthdays:
    months.append(birthdays[key][0:2])

# for each unique month, check how many times it repeats in the months array:
for month in set(months):
    month_count = months.count(month)
    # if a month repeats in the months array, more than one person has birthday in that month:
    if month_count != 1:
        print('Several persons were born in {}. month:'.format(month))
        # show persons that were born in the same month:
        for key in birthdays:
            if birthdays[key][0:2] == month:
                print(key)
    else:
        continue
