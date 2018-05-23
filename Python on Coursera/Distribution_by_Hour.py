name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
d = dict()
times = list()

for line in handle:
    if line.startswith('From '):
        # grab the time from the line
        time = line.split()[5]
        # grab only the hour from the time
        hour = time.split(':')[0]
        times.append(hour)

# create a dictionary where hours are keys and number of occurences of those hours are values
for hour in times:
    d[hour] = d.get(hour,0) + 1

for k,v in sorted(d.items()):
    print(k,v)
