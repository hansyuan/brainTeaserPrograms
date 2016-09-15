#prime families 
#replacing any n number of digits results in a family of prime numbers
# finding the smallest 8-digit prime whose family with 8 prime members

primes = [] 

def main():
    
    max = 15000000
    min = 10000000
    start = min
    increment = 5000000 # change to 10000000 for Surface Pro. Limit not needed for Asus

    while start < max:
        print("Starting: ", start)
        generatePrimes(start, start + increment)
        print(primes)
        #findFamily()

        start += increment

# need list of prime
def generatePrimes(min, max):  
    numbers = set(range(max,min,-1))

    for quick in range(0,25):
        if(isPrime(quick)):
            print(quick)
            numbers.difference_update(set(range(quick * 2, max+1, quick)))

    print(numbers)

    global primes
    primes = []
    
    """ generate a new sorted list of primes """
    while numbers:
        currNum = numbers.pop()
        if(isPrime(currNum)):
            primes.append(currNum)
            numbers.difference_update(set(range(currNum * 2, max+1, currNum)))
        
    primes.sort()
    

"""  n from 1 to 8, replace n digits of each prime 
number and see if there is a family of 8 """

def findFamily():
    # Pop from primes list.
    # Create Temp number
    # Change digits. If prime, count.
    # if count not 8, reset and go with next digit(s).


    lastDigit = 9 # It's really lastDigit-1

    while primes:
        currentPrime = primes.pop()


        for replaceLength in range(1,lastDigit): # for each length

            for startingPoint in range(0, lastDigit - replaceLength): # for each starting position
               

                for checkDigits in range(0,10): # for each num in decimal
                    primeAsChars = list(str(currentPrime))

                    for currentChange in range(startingPoint, startingPoint + replaceLength):
                        
                        replace = str(checkDigits)
                        primeAsChars[currentChange] = replace
                        
                checkPrime = "".join(primeAsChars)
                print (primeAsChars)
                print (checkPrime)

                return





# need check n is prime

def isPrimeOld(num):

    if(num == 1 or num == 0): return False

    for x in range (2,int(num/2+1)):
        if num%x == 0: return False

    return True


""" a better way of checking if a number is prime"""
def isPrime(n):
    if n == 0 or n == 1: return False

    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w

    return True


main()