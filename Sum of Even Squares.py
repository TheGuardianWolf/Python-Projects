def generateEven():
    evenList=[2]
    for i in evenList:
        g=i+2
        if g == 1002:
            break
        else:
            evenList.append(g)
    return evenList
    
def squareEven(x):
    squareList=[]
    for i in x:
        squareList.append(i*i)
    return squareList

def sumListNumbers(x):
    sum=0
    for i in x:
        sum+=i
    return sum

print(sumListNumbers(squareEven(generateEven())))
