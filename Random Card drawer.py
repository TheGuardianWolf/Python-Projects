import random
from decimal import *

instances=[0,0,0,0,0,0,0,0,0,0,0,0,0]
n=1
r=40

def drawCard():
    return random.randint(2,14)

def printing(n,rand,r):
    getcontext().prec=4
    if 104-n==0 and r==0:
        print(str(rand) + " " + str(r) + "/" + str(104-n) + "," + "0")
        return
    if rand < 11:
        print(str(rand) + " " + str(r) + "/" + str(104-n) + "," + str(Decimal(r*100)/Decimal(104-n)))
    if rand == 11:
        print("Jack,"+ str(r) + "/" + str(104-n) + "," + str(Decimal(r*100)/Decimal(104-n)))
    if rand == 12:
        print("Queen,"+ str(r) + "/" + str(104-n) + "," + str(Decimal(r*100)/Decimal(104-n)))
    if rand == 13:
        print("King,"+ str(r) + "/" + str(104-n) + "," + str(Decimal(r*100)/Decimal(104-n)))
    if rand == 14:
        print("Ace,"+ str(r) + "/" + str(104-n) + "," + str(Decimal(r*100)/Decimal(104-n)))

def checkInstance(rand):
    global instances
    if instances[rand-2] == 8:
        return False
    else:
        instances[rand-2] += 1
        return True

def checkImportant(rand):
    global r
    if r == 0:
        return False  
    elif rand > 9:
        r-=1
print("Card,Fraction,Percentage")
while n < 105:
    rand = drawCard()
    check = checkInstance(rand)
    if check == False:
        continue
    else:
        checkImportant(rand)
        printing(n,rand,r)
        n += 1

