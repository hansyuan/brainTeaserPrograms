import copy
currentPrime = 0
primes = []

def generatePrimesUpTo(max):
    global primes 
    primes = []
    primes.append(2)
    pool = set(range(3,max,2))
    while pool:
        p = pool.pop()
        primes.append(p)
        pool.difference_update(set(range(p*2, max + 1, p)))
    primes.sort()
    primes.reverse()

def nextPrime():
    global currentPrime
    global primes
    currentPrime = primes.pop()
    


""" a better way of checking if a number is prime"""
def isPrime(n):
    """Returns True if n is prime."""
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n % 3 == 0:return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0: return False

        i += w
        w = 6 - w

    return True



def generateChoices(digits):
    listOfBinaryLists = []

    # There are 2 ^ digits possibilities.
    for number in range(1, int((2**digits)/2)):
        binNum = list(str(bin(number)))

        holder = []
        for digit in range(0, digits):
            if binNum[-1] != 'b':
                holder.insert(0, binNum.pop())
            else:
                holder.insert(0,'0')
        listOfBinaryLists.append(holder)
    return listOfBinaryLists


def intToStrList(num):
    return list(str(num))

def strListToInt(strList):
    return int("".join(strList))

def hasFamily(number):
    currentNumber = intToStrList(number)
    length = len(currentNumber)
    configs = generateChoices(length)
   # #print(configs)

    for setting in configs:
        # create list of positions 
        positions = []
        count = 0
        strikes = 0
        #print(setting)

        for x in range(0,len(setting)):
         #   #print("Hello")
            if setting[x] == '1':
              #  #print("Trued")
                positions.append(str(x))

        for change in range(0,10):
           # #print (change)
            temp = copy.deepcopy(currentNumber)
            

            for digit in range(0,length):
                if str(digit) in positions:
                    temp[digit] = str(change)

            check = strListToInt(temp)
            #print ("Check: ", check)
          #  #print ("Chec2: ", currentNumber)
            if(isPrime(check)):
                count += 1
                #print("Is Prime, count ",count)
                if count == 7:
                    print(setting)
                    return True
            else:
                strikes += 1
                if strikes == 4:
                    #print("oops")
                    break
    return False



generatePrimesUpTo(2000000)
i = 0
while( True):

    nextPrime()
    i+=1
    if i % 10000 == 0: 
        print( "Current Prime: ", currentPrime)
    if hasFamily(currentPrime):
        print("FOUND: ", currentPrime)
        break

