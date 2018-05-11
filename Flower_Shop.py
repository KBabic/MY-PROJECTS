import random

sorts = ['rose', 'lily', 'orchid', 'gerber', 'tulip', 'lilac', 'dahlia']
colors = ['red', 'white', 'yellow', 'purple', 'pink']

class Flower:
    '''
    Single Flower
    '''
    def __init__(self, sort, color):
        self.sort = sort
        self.color = color

    def __str__(self):
        return self.color + ' ' + self.sort

class Selection:
    '''
    Entire flower assortment in the shop
    '''
    def __init__(self):
        self.selection = []
        counter = 0
        for counter in range(10):
            for color in colors:
                for sort in sorts:
                    self.selection.append(Flower(sort, color))
                    counter += 1
    def __str__(self):
        assortment = ''
        for flower in self.selection:
            assortment = assortment + '\n' + flower.__str__()
        return 'The assortment of flowers:' + assortment

    def shuffle(self):
        random.shuffle(self.selection)

    def deal(self):
        single_flower = self.selection.pop()
        return single_flower

    def track(self):
        for flower in self.selection:
            num_flowers = self.selection.count(flower)
            if num_flowers == 5:
                print('There are only 5 remaining pieces of {}! Place an order.'.format(flower))
            else:
                print('There are {} of {} left.'.format(num_flowers, flower))

class Bouquet:
    '''
    Bouquet containing odd number of flowers: 3,5 or 7
    '''
    def __init__(self):
        self.bouquet = []
    def add_flowers(self,flower):
        self.bouquet.append(flower)
    def __str__(self):
        bouquet = ''
        for flower in self.bouquet:
            bouquet += '\n' + str(flower)
        return 'Bouquet contains:' + bouquet

def make_bouquet(selection, bouquet):
    '''
    Function defines number of flowers in a Bouquet,
    shuffles Selection that many times,
    takes that many flowers from selection,
    adds that many flowers to bouquet
    '''

    num_flowers = random.randint(3,7)
    if num_flowers % 2 == 0:
        num_flowers += 1
    for i in range(1,num_flowers+1):
        selection.shuffle()
        flower_item = selection.deal()
        bouquet.add_flowers(flower_item)



testSelection = Selection()
testBouquet = Bouquet()
make_bouquet(testSelection, testBouquet)
print(testBouquet)
print('\n')
testSelection.track()
