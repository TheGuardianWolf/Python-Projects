isPrime=[True]*2000001
isPrime[0]=False
isPrime[1]=False
count=0
for i in range(2,2000001):
   if isPrime[i]==True:
      count+=i
      for x in range(i,2000001):
         if i*x>=2000001:
            break
         else:
            isPrime[i*x]=False
print(count)
