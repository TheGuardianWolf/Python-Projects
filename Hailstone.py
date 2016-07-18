count=0
maxx=0
def hailstone(n):
   global count
   if n==1:
      count+=1
      return 1
   else:
      if n%2==0:
         count+=1
         return hailstone(n/2)
      else:
         count+=1
         return hailstone(n*3+1)


for n in range(1,101):
   hailstone(n)
   if count>maxx:
      print("Largest hailstone length=",count,"Produced by=",n)
      maxx=count
   count=0
      
