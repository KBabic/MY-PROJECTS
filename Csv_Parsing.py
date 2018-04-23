import csv

f1 = open('Example 1.csv')
csv_f = csv.reader(f1)
attendees1 = []

for row in csv_f:
    attendees1.append(row[2])

f1.close()

f2 = open('Example 2.csv')
csv_f = csv.reader(f2)
attendees2 = []

for row in csv_f:
    attendees2.append(row[2])

f2.close()

attendees1 = set(attendees1)
attendees2 = set(attendees2)

print('Attendees of the first event were:\n')
list(map(lambda attendee: print(attendee), attendees1))
    
print('\nAttendees of the second event were:\n')
list(map(lambda attendee: print(attendee), attendees2))

# THIS PART NEEDS REFACTORING(!):

if len(attendees2) > len(attendees1) :
    print('\nSecond event had more attendees.')
    print('New attendees were:',list(map(lambda attendee: print(attendee), attendees2.difference(attendees1))))
    if len(attendees1.difference(attendees2)) > 0:
        print('Attendees of the first event who skipped second event are:',list(map(lambda attendee: print(attendee),attendees1.difference(attendees2))))

elif len(attendees1) > len(attendees2):
    print('\nFirst event had more attendees.')
    print('Second time the following people did not come:',attendees1.difference(attendees2))
    if len(attendees2.difference(attendees1)) > 0:
        print('New attendees were:',list((map(lambda attendee: print(attendee),attendees2.difference(attendees1)))))

elif len(attendees1) == len(attendees2):
    print('\nBoth events had equal number of participants')
    print('Following people visited both events:',attendees1.intersection(attendees2))
