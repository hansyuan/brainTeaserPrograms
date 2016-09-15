# find the 10001th prime number
# while there are less than 10001 elements in a list, keep adding prime numbers

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

listPrimes = []
num = 2
rank = 10001
rank = 6
found = 0

while found < rank:
#	print (found)
	if(isPrime(num)):
		found += 1
	num+=1

print (num) 
