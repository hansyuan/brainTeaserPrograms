# for fun

max = 100000000000


list = []
primes = []
hashm = {}

print("starting allocation")

for x in range (0, max):
    list.append(x)
    if x % 10000000 == 0: print(x)


print("finished allocating")
print("doing random stuff")
"""
while list:
    x = list.pop()
    primes.append(x)
    list.difference_update(set(range(x * 2, max + 1, x)))
    """

print(primes)
print("all done!")

