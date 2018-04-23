while True:
    try:
        cost = float(input("Please enter the cost in dollars: ")) 
        break
    except:
        print("Please enter the cost as number with '.' as separator for decimals!")

while True:
    
    while True:
        try:
            payment = float(input("\nEnter your payment in dollars: "))  
            break
        except:
            print("Please enter your payment aas number with '.' as separator for decimals!")

    if payment < cost:
        print("\nYour payment is insufficient! Please try again. ")
        break
    else:
        print('\nYour payment is',payment,'dollars.')
        break

import math

change_amount = payment - cost
change_dollars = math.floor(change_amount)
change_cents = round((change_amount - change_dollars) * 100)

class Change:
    
    def __init__(self,change_dollar,change_cent):
        self.change_dollar = change_dollar
        self.change_cent = change_cent
    
    def quarter(self):
        return self.change_cent // 25
    
    def dime(self):
        return (self.change_cent % 25) // 10
    
    def nickle(self):
        return ((self.change_cent % 25) % 10) // 5
    
    def penny(self):
        return ((self.change_cent % 25) % 10) % 5

change = Change(change_dollar=change_dollars,change_cent=change_cents)

if change.change_dollar != 0 or change.change_cent != 0:
    
    print("\nPlease take your change:\n")

    if change.change_dollar > 0:
        print("dollars:",change.change_dollar)
    else:
        pass
    if change.quarter() > 0:
        print("quarters:",change.quarter())
    else:
        pass
    if change.dime() > 0:
        print("dimes:",change.dime())
    else:
        pass
    if change.nickle() > 0:
        print("nickles:",change.nickle())
    else:
        pass
    if change.penny() > 0:
        print("pennies:",change.penny())
    
print('\nThank you and come again!')