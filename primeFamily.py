#prime families 
#replacing any n number of digits results in a family of prime numbers
# finding the smallest 8-digit prime whose family with 8 prime members

primes = []

def main():
    
    max = 100000000
    min = 10000000
    start = min
    increment = 10000000 # change to 10000000 for Surface Pro. Limit not needed for Asus

    while start < max:
        

        received = generatePrimes(start, start + increment)
        print(start)

        start += increment

# need list of prime
def generatePrimes(min, max):  
    numbers = set(range(max,min,-1))
    global primes
    primes = []
    # pop a number from primes
    # check if prime
    # yes: add to primes and remove all multiples from numbers
    while numbers:
        currNum = numbers.pop()
        primes.append(currNum)
        numbers.difference_update(set(range(currNum * 2, max+1, currNum)))
        #print(len(numbers))
    

# need check n is prime

def isPrimeOld(num):

    if(num == 1 or num == 0): return False

    for x in range (2,int(num/2+1)):
        if num%x == 0: return False

    return True


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


main()