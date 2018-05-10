import csv
import operator

participants = open('C:\\Users\\Kaja\\Desktop\\MY-PROJECTS\\sample_participants.csv')
raw_reader = csv.reader(participants)
raw_data = []
for row in raw_reader:
	raw_data.append(row)

sort1 = sorted(raw_data[1:], key=operator.itemgetter(0,1,2,3))
sort1.insert(0, raw_data[0])

updated_participants = open('C:\\Users\\Kaja\\Desktop\\MY-PROJECTS\\updated_participants.txt','w+')

item_lengths = []
for row in sort1:
	for item in row:
		item_length = len(item)
		item_lengths.append(item_length)

for row in sort1:
	for item in row:
		updated_participants.write(item + ' ' * (max(item_lengths) - len(item)))
	updated_participants.write('\n')

participants.close()
updated_participants.close()
