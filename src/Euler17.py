# Author: Jayden Navarro
# Date: 10/12/2015

s10 = [ "one", "two", "three", "four", "five", "six", "seven", 
        "eight", "nine" ]
s20 = [ "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", 
        "sixteen", "seventeen", "eighteen", "nineteen" ]
s100 = [ "twenty", "thirty", "forty", "fifty", "sixty", "seventy", 
         "eighty", "ninety" ]

l10 = 0
for i in s10:
   l10 += len( i )

l20 = l10
for i in s20:
   l20 += len( i )

l100 = l20
for i in s100:
   l100 += len( i ) * 10 + l10

l1000 = l100
for i in s10:
   l1000 += len( i + "hundred" )
   l1000 += len( i + "hundred" + "and" ) * 99 + l100 

l1000 += len( "one" + "thousand" )

print( l1000 )
