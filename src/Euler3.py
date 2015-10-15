# Author: Jayden Navarro
# Date: 10/12/2015

import math

num = 600851475143
notPrime = set()
for i in range(2, int(math.sqrt(num)) + 1):
   if i not in notPrime:
      for j in range(2, int(math.sqrt(num)) + 1):
         temp = {i*j}
         notPrime.update(temp)
