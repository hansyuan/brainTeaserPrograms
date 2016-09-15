
currentPrime = 1

def nextPrime():
    global currentPrime
    currentPrime += 1
    while(not isPrime(currentPrime)): currentPrime += 1
    return currentPrime




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
    for number in range(0, 2 ** digits):
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


