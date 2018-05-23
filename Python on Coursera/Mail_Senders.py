name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
senders = list()
ddd = dict()
for line in handle:
    # take only lines that start with the word 'From '
    if line.startswith('From '):
        senders.append(line.split()[1])
# create a dictionary with either incrementing existing value of a key or creating a key and dedicating value of 1
for sender in senders:
    ddd[sender] = ddd.get(sender, 0) + 1
# print out the person who sent the greatest number of emails:
for key in ddd:
    if ddd[key] == max(ddd.values()):
        print(key, ddd[key])

# another way of finding the max value:

# largest = -1
# for k,v in ddd.items():
#   if v > largest:
#       largest = v
