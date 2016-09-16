import math
# find next number in sequence


# find all divisors of this numbers and count

# if more than n, return this number.

def numDivisors(num):
    count = 0
    for x in range(1, int(math.sqrt(num)) ): 
        if num % x == 0:
            count += 1
    return count*2

n = 500
currNum = 0
increment = 1
while True: 
    currNum += increment
    increment += 1
    if n < numDivisors(currNum):
        print (currNum)
        break

