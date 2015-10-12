# Author: Jayden Navarro
# Date: 10/12/2015

previous = 1
current = 2
evenSum = 2
while current <= 4000000:
    temp = previous
    previous = current
    current += temp
    if (current % 2 == 0):
        evenSum += current
print(evenSum)
