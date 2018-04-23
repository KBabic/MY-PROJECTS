import math

while True:
    try:
        print(round(math.pi,int(input("How many decimals for PI do you need? Please enter an integer:  "))))
        break
    except:
        continue