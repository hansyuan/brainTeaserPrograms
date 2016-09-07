# Python program to test the probability game. 

# Two buckets, 100 black marbles and white marbles each. 
# How to maximize chance of choosing one type of marble? 
# Picking a choice is represented by using the random 
# number mod the total number of marbles in the bucket. 
import random

print ("There are 100 white marbles and 100 black marbles. ")
print ("And there are two buckets that will contain those marbles.")
print ("All marbles will be used.")
print ("Allocate the marbles in each bucket such that you have the highest")
print ("probability of getting the white marble.")
print ("Each bucket has an equal chance of getting chosen. ")
print ()
userInput = False
redo = True

while redo:

	if userInput:
		numWhiteFirst = int(input("Number of white marbles in the first bucket:\n"))
		numBlackFirst = int(input("Number of black marbles in the first bucket:\n"))
		numWhiteSec = int(input("Number of white marbles in the second bucket:\n"))
		numBlackSec = int(input("Number of black marbles in the second bucket:\n"))

	else:
		numWhiteFirst = 1
		numBlackFirst = 0
		numWhiteSec = 99
		numBlackSec = 100

	firstTotal = numWhiteFirst + numBlackFirst
	secondTotal = numWhiteSec + numBlackSec

	if numWhiteFirst+numWhiteSec != 100 \
	or numBlackFirst+numBlackSec != 100 \
	or secondTotal+firstTotal != 200:
		print ("\nThere are 100 white and 100 black marbles.")
		redo = True
	else: 
		redo = False



whiteChosen = 0
blackChosen = 0



numIterations = 15000000


for x in range(0, numIterations):
	#print("hi")
	bucket = random.randint(0,1)

	if bucket == 0:
		picked = random.randint(0,firstTotal-1)
		if picked < numWhiteFirst:
			whiteChosen += 1
		elif picked < firstTotal:
			blackChosen += 1
		else:
			print("This shouldn't happen. 1.")

	elif bucket == 1:
		picked = random.randint(0,secondTotal-1)
		if picked < numWhiteSec:
			whiteChosen += 1
		elif picked < secondTotal:
			blackChosen += 1
		else:
			print("This shouldn't happen. 2.")

	else:
		print("This shouldn't happen either. 3.")

whiteAvg = whiteChosen/numIterations
blackAvg = blackChosen/numIterations

print("White Avg: ", str(whiteAvg))
print("Black Avg: ", str(blackAvg))



