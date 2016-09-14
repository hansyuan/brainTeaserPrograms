#math.py
mults = []

for x in range(0,1000):
	if x%3 == 0 or x%5 == 0:
		mults.append(x)

sum = 0
for x in mults:
	sum += x

print ("Sum: ", sum)