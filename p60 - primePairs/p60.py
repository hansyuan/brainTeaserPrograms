def generatePrimesUpTo(max):
    primes2=[]
    tempPrimes = []
    primes = {}
    primes[2] = 3
    oldP = 3
    pool = set(range(3,max,2))
    while pool:
        p = pool.pop()
        tempPrimes.append(p)
        pool.difference_update(set(range(p*2, max + 1, p)))
    tempPrimes.sort()
    #tempPrimes.reverse()
    prev = 2
    while tempPrimes:
        popped = tempPrimes.pop()
        primes[prev] = popped
        #print(prev," ", popped)
        prev = popped
    for i in primes:
        primes2.append(i)
    primes2.sort()
    return primes2


def concatInts(num, num2):
    return int(str(num) + str(num2))


def checkPair(li, num, num2):
    if not concatInts(num,num2) in li:
        return False
    return (concatInts(num2, num) in li)


def analyzePrime(num):
    #




x = generatePrimesUpTo(100000)
print(checkPair(x,3, 109))
#print (x)

