from IPython.display import clear_output

# conversions = {type of conversion offered: units offered}

conversions = {'currency':['EUR','USD','GBP','JPY','CHF','RUB'],
'temperature':['C','F'],
'mass':['mg','g','kg','carat','ounce','pound','t'],
'volume':['cm3','m3','ml','l','pints','gallons','cubic inches','barrels'],
'time':['s','min','h','days','weeks','months','years'],
'speed':['km/h','m/s','mph','mps','yards/h','yards/s','nautical miles/h'] }

print('Please enter the type of the conversion. The following are offered:')
for key in conversions.keys():
    print(key)
print('\n')

while True:
    conversion = input()
    if conversion in conversions.keys():
        break
    else:
        print('Please enter only one of the offered types of the conversion.')

def choose_unit(conversion):
    offered_units = conversions[conversion]
    for unit in offered_units:
        print(unit)


print('\nPlease choose a unit to convert from. The following are offered:')
choose_unit(conversion)

def check_unit():
    while True:
        unit = input()
        if unit in conversions[conversion]:
            return unit
            break
        else:
            print('Please enter only one of the offered units.')

unit1 = check_unit()

# remove the chosen unit from list of offered units (makes no sense to convert from EUR to EUR):
conversions[conversion].pop(conversions[conversion].index(unit1))

print('\nPlease choose a unit to convert to. The following are offered:')
choose_unit(conversion)

unit2 = check_unit()

#list of units needs to be updated again with the unit which was popped out, because we need original list for later calculation:
conversions[conversion].append(unit1)

# now unit_1 and unit_2 need to be passed to the calculation part
# convert unit_1 to a base unit and then convert base unit to unit_2

base_units = {'currency':'EUR','temperature':'C','mass':'kg','volume':'l','time':'h','speed':'km/h'}
base_unit = base_units[conversion]

conv_values = {'EUR':{'EUR':1,'USD':1.23,'GBP':0.88,'JPY':132.59,'CHF':1.20,'RUB':75.57},
 'C':{'C':1,'F':33.8},
 'kg':{'mg':1000000,'g':1000,'kg':1,'carat':5000,'ounce':35.274,'pound':2.2046,'t':0.001},
 'l':{'cm3':1000,'m3':0.001,'ml':1000,'l':1,'pints':2.11,'gallons':0.26,'cubic inches':61.02,'barrels':117.348},
 'h':{'s':3600,'min':60,'h':1,'days':0.0417,'weeks':0.00595,'months':0.00137,'years':0.000114},
 'km/h':{'km/h':1,'m/s':0.2778,'mph':0.6213,'mps':0.000173,'yards/h':1093.61,'yards/s':0.3038,'nautical miles/h':0.53996} }

value_1 = conv_values[base_unit][unit1]
value_2 = conv_values[base_unit][unit2]

while True:
    try:
        inserted_value = float(input('\nPlease enter the value for the conversion: '))
        break
    except:
        print('Value needs to be a number!')


converted_value = inserted_value / value_1 * value_2

print('\nThe result is: ',round(converted_value,4))
