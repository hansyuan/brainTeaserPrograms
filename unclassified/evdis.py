#takes too long
def find():
	check = 0
	go = True
	while go:
		go = False
		check += 1
		for num in range (1,21):
			if(check%num>0):
				go = True
		
	return check
			
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


#failed
def find2():
	debug = True


	mult = []
	
	for num in range(-20,0):

		num = num*(-1)
		if debug:
			print("Curr: ", num)

		# check if primes are used already.
		# if not, add them

		tempNum = num
		if debug:
			print(tempNum)

		#find all the primes
		while(not isPrime(tempNum)):
			if debug:
				print("while loop")

			check = 2
			while check < tempNum:

				if debug:
					print(tempNum, "| ", check)

				if tempNum % check == 0:
					print(tempNum % check)
					if check not in mult:

						if debug:
							print ("Confusion: ",check)
	
						mult.append(check)

					tempNum = int(tempNum / check)
					check = 2
				check+=1
					
						

		#		if check == tempNum - 1:
		#			print ("breaking")
		#			break
					
			#reduce the num if needed
		
			# the only way it can reach this is if 
			# tempnum is a prime number hopefully
		if tempNum not in mult:
			print(tempNum)
			mult.append(check)

	print (mult)
	ret = 1
	for x in mult:
		ret *= x
		print (ret)

	return ret


#this function will return the number that is divisible evenly
#by numbers ( 1 through n ) where n is a specified int	


def leastDivEv(n):
	debug = False


	considered = []

	currentNumber = 1
	while currentNumber <= n:
		if debug: 
			print(currentNumber)

		# if the number is prime, it is accepted
		if isPrime(currentNumber):

			if debug: 
				print("Is Prime, adding")

			considered.append(currentNumber)

		#if not prime, find it's prime factors and consider it
		else:

			checkDiv = 2
			currentNumber2 = currentNumber

			while checkDiv <= currentNumber2:
				if debug: 
					print(currentNumber2,"|",checkDiv)


				if currentNumber2 % checkDiv == 0:

					if checkDiv not in considered:
						if debug: 
							print(checkDiv, " was added.")

						considered.append(checkDiv) 
					#print("This should happen: ")
					currentNumber2 = int(currentNumber2 / checkDiv)
					checkDiv = 2
				else:
					checkDiv += 1

		currentNumber += 1

	ret = 1
	print (considered)
	for num in considered:
		ret *= num
		print (ret)

	return ret

# Main Method:
wantedValue = leastDivEv(20)
print(wantedValue)