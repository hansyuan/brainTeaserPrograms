# find a^2 + b^2 = c^2 such that a+b+c = 1000

# make a list of all perfect squares up to 1000^2
import math
def perf_sq(n):
    return n == int(math.sqrt(n)) * int(math.sqrt(n))


def do():
	square = {}

	for x in range( 1, 1000):
		square[x] = x**2

	#print (square)
	for x in square:
		for y in square:
			if perf_sq( x**2 + y**2 ) :
				z =  math.sqrt( x**2 + y**2 )
				if z < 1000:
					#print("Pyth:"+ '\t', str(x), '\t', str(y) ,'\t', str(z))
					if x + y + z == 1000:
						print (x,"\t", y ,"\t", z, "\t", x*y*z)
						

"""
for x in range( 0, 99999):
	prints = perf_sq(x)
	if prints:
		print (x)
		"""


do()