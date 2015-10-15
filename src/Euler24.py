# Author: Jayden Navarro
# Date: 10/12/2015

import math

l = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]

count = 0

def printList( l ):
   s = ""
   for i in l:
      s += str( i )
   return s

def permute( l, loc ):
   if len( l ) == 1:
      return l
   passing = []
   build = []
   pos = int( math.ceil( float( loc ) / float( 
      perms( len( l ) - 1 ) ) ) )
   for i, c in enumerate( l ):
      if i != pos - 1:
         passing.append( c )
   build.append( l[ pos - 1 ] )
   build += permute( passing, loc - ( pos - 1 ) * 
      perms( len( l ) - 1 ) )
   return build

def perms( n ):
   factorial = n
   for i in range( n-1, 1, -1 ):
      factorial *= i
   return factorial

print( printList( permute( l, 1000000 ) ) )
