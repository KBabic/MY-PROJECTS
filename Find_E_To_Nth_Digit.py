import math

while True:
    try:
        print(round(math.e,int(input("How many decimals for e do you need? Please enter an integer:  "))))
        break
    except:
        continue