"""
For each number from 1 to n, you need to consider all its prime factorials.
Your multiples might have the correct number of each prime! 

Use a global hashmap and then a temporary hashmap


"""
def isPrime(num):
	if(num == 1 or num == 0):
	#	print("0, 1 not primes.")
		return False

	for x in range (2,num):
		if num%x == 0:
	#		print(num, " is not prime.")
			return False

	#print (num, " is a prime.")
	return True


# This method returns the primes as key and the number of those primes as value.
def primeCounts(thisNum):
	debug = False
	tempHash = {}
	possiblePrime = 2
	if debug: print (thisNum)

	while possiblePrime <= thisNum:
		if debug: print (thisNum,"\t",possiblePrime)

		if thisNum % possiblePrime == 0:
			if possiblePrime not in tempHash:
				tempHash[possiblePrime] = 1
			else:
				tempHash[possiblePrime] += 1
			thisNum = int(thisNum / possiblePrime)
			possiblePrime = 2
		else:
			possiblePrime += 1

	#print (tempHash)
	return tempHash

# Given the primes and their number of occurrences, update the global prime and numbers.
def update(hashmap):
	global considered 
	for element in hashmap:
		if element not in considered:
			considered[element] = hashmap[element]
		else:
			if considered[element] < hashmap[element]:
				considered[element] = hashmap[element]

""" 

Main starting point 

""" 
considered = {}
n = 20
curr = 0
total = 1

while curr < n:
	curr += 1
	# find all the primes and the number of each
	counts = primeCounts ( curr )
	update(counts)

#print (considered)
for prime in considered:
	mult = 1
	for iterations in range (0,considered[prime]):
		mult *= prime
	total *= mult

print (total)
