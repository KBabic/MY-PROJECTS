import csv
import operator

participants = open('C:\\Users\\Kaja\\Desktop\\MY-PROJECTS\\sample_participants.csv')
raw_reader = csv.reader(participants)
raw_data = []
for row in raw_reader:
	raw_data.append(row)

sort1 = sorted(raw_data[1:], key=operator.itemgetter(0,1,2,3))	
for row in sort1:
	print(row)

participants.close()
