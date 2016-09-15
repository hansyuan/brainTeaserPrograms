#sum of primes below n



def isPrime(num):
	if(num == 1 or num == 0): return False

	for x in range (2,num):
		if num%x == 0: return False

	return True

def primesUpTo2(n):
	global prime
	total = 0
	for num in range (2,n):
		if num not in prime:
			if(isPrime(num)):
				prime[num] = True
				multiply = 2
				composite = num * multiply
				while composite < n:
					prime[composite] = False
					multiply += 1
					composite = num * multiply
					#print(composite)



			#listOfPrimes.append(num)
			print(num)
			total += num
	return total

def primesUpTo(n):
	numbers = set(range(n, 1, -1))

	primes = []
	while numbers:
		p = numbers.pop()
		primes.append(p)
		numbers.difference_update(set(range(p*2, n+1, p)))
	return primes

def main():
	global prime 
	prime = {}
	max = 2000000

	#for x in range (0, max):
	#	prime[x] = False

	#print( primesUpTo(10))	
	listP = primesUpTo(max)
	total = 0
	for x in listP:
		total += x
	print (total)



main()