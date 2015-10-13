# Author: Jayden Navarro
# Date: 10/12/2015

def isPalindrome( n ):
	s = str( n )
	return s == s[ :: -1 ]

high = -1

for i in range( 999, 100, -1 ):
	for j in range( 999, 100, -1 ):
		if isPalindrome( j * i ) and j * i > high:
			high = j * i

print( high )
