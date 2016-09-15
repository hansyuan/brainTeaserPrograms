"""
methods needed:
- generate a list of prime numbers given the range
    * use global list to avoid copying
- determine if number is prime
- given a number, check every combination of its number 
    for example: the prime number 103 will need to replace 1, 0, and 3 as follows:
        for each lengthChange 1 2 3:
            for each starting point between 0 and number length - lengthChange
                for each combination of lengthChange (for example, there is one way to change 3 digits
                in a 3 digit number. And there are three ways to change 1 digit in 3 digit number.)




"""

""" global variables """ 


""" methods """
primeList = []


""" a better way of checking if a number is prime"""
def isPrime(n):
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


# Generates a sorted list of primes between min and max. 
def generatePrimes(min, max):  
    numbers = set(range(min,max,1))
    global primeList
    primeList = []
    
    """ generate a new sorted list of primes """
    while numbers:
        currNum = numbers.pop()
        if(isPrime(currNum)):
            primeList.append(currNum)
            numbers.difference_update(set(range(currNum * 2, max+1, currNum)))
    primeList.sort()

# pop each prime out and then check its Prime Family
def checkPrimes():
    global primeList
    primeList = {973}

    maxLength = 8
    while primeList:
        currentPrime = primeList.pop()
        currPrimeStr = list(str(currentPrime))
        currLength = len(currPrimeStr)
        print("Current Prime and Length: ", currentPrime, currLength)

        #For each length
        for length in range(1, maxLength):

            #For Starting Point
            for position in range(0,currLength):


                print("Position and changeLength: ", position, length)

                if length == currLength:
                    break

                #print("Current digit is ", digit)

                for digit in range(0,10):
                    tempStr = currPrimeStr
                    tempStr[position] = str(digit)

            print (tempStr)


def main():
    generatePrimes(2, 100)
    checkPrimes()

""" call main """
main()