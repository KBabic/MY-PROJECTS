from random import shuffle
coin = ['head', 'tale']
counter = 0
result = []
num_of_flips = int(input('How many times do you want to flip coin: '))

for num in range(1,num_of_flips+1):
	shuffle(coin)
	counter += 1
	result.append(coin[0])

print(result)
print('Number of heads is:',result.count('head'))
print('Number of tails is:',result.count('tale'))

