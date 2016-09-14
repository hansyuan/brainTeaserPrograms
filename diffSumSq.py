n = 100

sum = 0
square_Sums = 0
sum_Squares = 0

for x in range( 1, n+1):
	sum += x
	sum_Squares += (x**2)

square_Sums = sum**2

print ("SqSums ",square_Sums,"\t","SumSqs ",sum_Squares)
print (square_Sums - sum_Squares)