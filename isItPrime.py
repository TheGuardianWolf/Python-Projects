def isItPrime(N): # same as before
  for D in range(2, N):
    if (D * D > N):          # first added line
      break                  # second added line
    if N % D == 0:
      return False
  return True
