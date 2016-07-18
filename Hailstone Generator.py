def hailstoneGen(n,r):
    global hailstoneList
    hailstoneList.append(n)
    if n==1:
      r+=1
      print(hailstoneList)
      print("Number Count="+str(r))
      return r
    else:
      if n%2==0:
         r+=1
         hailstoneGen(int(n/2),r)
      else:
         r+=1
         hailstoneGen(n*3+1,r)

for i in range(1,10):
    hailstoneList=[]
    print("Number="+str(i))
    hailstoneGen(i,0)
