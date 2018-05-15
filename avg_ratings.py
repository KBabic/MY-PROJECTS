# The input file contains three columns: id - a unique identifier for each row, year - the year and quarter of the rating, and rating - the approval rating.
# Write output to a new CSV with three columns:
#   year will contain whole years (i.e., 1975 but no information about specific quarters),
#   mean will have the mean approval rating for that year,
#   median will have the median approval rating for that year.
# As some quarters are missing ratings (NA) you will have to exclude those from the mean/median calculations.

import csv
import statistics

csv_file = open('C:\\Users\\Kaja\\Desktop\\MY-PROJECTS\\presidents.csv')
content = csv.reader(csv_file)
# this line enables reading the csv multiple times without open/close each time:
data = [row for row in content]
csv_file.close()
years = list()
# dictionary where key is year and value is list of ratings for that year:
d = dict()

for row in data:
    #starting from the second row:
    if row[1][0:4] != 'year':
        year = row[1][0:4]
        years.append(year)

# for each unique year give me list of all ratings:
for year in set(years):
    d[year] = list()
    for row in data:
        if row[1][0:4] == year and row[2] != 'NA':
            d[year].append(int(row[2]))
# print(d)

means = dict()
for year in d:
    means[year] = round(sum(d[year])/len(d[year]),2)
# print(means)

medians = dict()
for year in d:
    medians[year] = round(statistics.median(d[year]),2)
# print(medians)

output_file = open('C:\\Users\\Kaja\\Desktop\\MY-PROJECTS\\presidents_output.txt','w+')
output_file.write('year,mean,median\n')
# writing rows to output file sorted by years (ascending order):
for year in sorted(d.keys()):
    output_file.write(year+','+str(means[year])+','+str(medians[year])+'\n')
output_file.close()
