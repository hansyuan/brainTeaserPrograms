#Python progam to find the largest palindrome 
#from x*y where x and y are three digit numbers

largest = 0;

for x in range (0,1000):
	for y in range (x,1000):
		isPalindrome = True;
		pro = list(str(x*y));
		#print(x*y, " ", len(pro))
		length = len(pro)
		for curr in range(0,int(length/2)):
			#print ( pro[curr], " ", pro[length-1-curr])
			if pro[curr] != pro[length-1-curr]:
				isPalindrome = False
				break

		if isPalindrome:
			if largest < x*y:
				largest = x*y 

print (largest)




