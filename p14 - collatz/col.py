# def collatz sequence, ensure correctness. 
# returns amount of changes before hitting 1


# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

def collatz(num):
    count = 1

    while not num == 1:
        count+=1
        if num % 2 == 0: num /= 2
        else: num = (3*num)+1
    return count

highest = 0
start = 0
for x in range(1, 1000000):
    t = collatz(x)
    if highest < t:
        highest = t
        start = x

print (start)