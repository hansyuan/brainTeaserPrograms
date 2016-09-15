import copy
currentPrime = 2
primes = {}
primes2 = set()

def generatePrimesUpTo(max):
    global primes, primes2
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
    tempPrimes.reverse()
    prev = 2
    while tempPrimes:
        popped = tempPrimes.pop()
        primes[prev] = popped
        #print(prev," ", popped)
        prev = popped
    for i in primes:
        primes2.add(i)



def nextPrime(num):
    global currentPrime
    global primes
    return primes[num]
    
def nextPrimeFrom():
    global currentPrime
    while(not isPrime(currentPrime)):
        currentPrime+=1



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
    for number in range(1, int((2**digits))):
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
    global primes

    familyMembers = 8

    currentNumber = intToStrList(number)
    length = len(currentNumber)
    configs = generateChoices(length)
   # #print(configs)

    for setting in configs:
        # create list of positions 
        positions = []

        passed = []
        count = 0
        strikes = 0
       # print(setting)

        for x in range(0,len(setting)):
         #   #print("Hello")
            if setting[x] == '1':
              #  #print("Trued")
                positions.append(str(x))


        change = 10
 #grab the lowest digit and start change from there
        temp = copy.deepcopy(currentNumber)
        for digit in range(0, length):
            if str(digit) in positions:
                if change > int(temp[digit]):
                    change = int(temp[digit])



      #  for change in range(0,10):
        change -= 1
        while change < 10:
            change += 1
            
           # #print (change)
            
           
        
            temp = copy.deepcopy(currentNumber)
            

            for digit in range(0,length):
                if str(digit) in positions:
                    temp[digit] = str(change)

            check = strListToInt(temp)
            #print ("Check: ", check)
          #  #print ("Chec2: ", currentNumber)
            if check in primes2 and check > currentPrime:
                count += 1
                passed.append(check)
            #    print("Is Prime, count ",count)
                if count == familyMembers:
                    print(setting)
                    for x in passed:
                        print (x)
                    return True
            #else:
                #strikes += 1
               # if strikes > 10 - familyMembers:
              #      print("oops")
             #       break
    return False


nextPrimeFrom()
generatePrimesUpTo(100000000)

founded = 0
while( True):


    currentPrime = primes[currentPrime]
    #print("\n")
    if hasFamily(currentPrime):
        print("FOUND: ", currentPrime)
        print("\n")
        founded += 1
        if founded == 3:
            break;
        



   
