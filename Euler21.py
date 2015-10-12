# Author: Jayden Navarro
# Date: 10/12/2015

def sumDivisors( n ):
	sum = 0
	for i in range( 1, n ):
		if n % i == 0:
			sum += i
	return sum

def isAmicable( n ):
	dN = sumDivisors( n )
	if ( dN != n ):
		return n == sumDivisors( dN )
	else:
		return False

sum = 0
for i in range( 1, 10000 ):
	if isAmicable( i ):
		sum += i

print( sum )
