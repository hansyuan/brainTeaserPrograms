def fact(n):
    if n == 1: 
        return 1
    else:
        return n*fact(n-1)

x = [int(y) for y in list(str(fact(100)))]
i = 0
for z in x:
    i += z
print (i)