import math

def divisorsSummed(num):
    divs = []
    for div in range(1, int(math.sqrt(num))):

        if num % div == 0:
            divs.append(div)
            if num/div < num: divs.append(num/div)
            #print(div, num/div)
    sum = 0
    for div in divs: 
        sum += div

    return( int(sum) )

print(divisorsSummed(220))
numPairs = list()
found = list()


for x in range(1,20000):
    y = divisorsSummed(int(x))
    if x == divisorsSummed(y) and x != y:
        print (x,y)
        numPairs.append(x)

print ("numpairs: ", numPairs)

for z in numPairs:
    if z < 10000:
        found.append(z)
print (found)

sum = 0
for z in found:
    sum += z

print(sum)