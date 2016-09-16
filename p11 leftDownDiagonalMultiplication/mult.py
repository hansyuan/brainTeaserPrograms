# read each line of the file, then determine largest product

""" All data structures and method calls are here. """
def main():
    lists = read2DArray("input.txt") 
    print (lists)
    x = findLargestProduct(lists, 4)
    print (x)



""" Read in the 2D Array from the file and return a list of lists. """ 
def read2DArray(name):
    input = open(name,"r")
    lists = list(list())

    # While there are still lines being read, continue. 
    while(True):
        file = input.readline()
        if len(file) == 0: return lists
        file = file.replace('\n',"")
        array = [int(x) for x in file.split (" ")]
        lists.append(array)



"""Call all the mult methods """
def findLargestProduct(lists, numProducts):
    debug = True
    numProducts -= 1
    largest = 0
    size = len(lists)
    if debug: products = []


    # make all the calls to MultRight
    for row in range(0, size):
        for col in range(0, size - numProducts):
            compVal = multRight(lists, row, col)
            if largest < compVal: largest = compVal
            if debug: 
                print(compVal)
                products.append(compVal)


    for col in range(0, size):
        for row in range(0, size - numProducts):
            compVal = multDown(lists, row, col)
            if largest < compVal: largest = compVal
            if debug: 
                print(compVal)
                products.append(compVal)


    for col in range(0, size - numProducts):
        for row in range(0, size - numProducts):
            compVal = multDR(lists, row, col)
            if largest < compVal: largest = compVal
            if debug: 
                products.append(compVal)
                print(compVal)


    for row in range(0, size - numProducts):
        for col in range(numProducts, size):
            compVal = multDL(lists,row,col)
            if largest < compVal: largest = compVal
            if debug: 
                products.append(compVal)
                print(compVal)

    if debug: 
        products.sort()
        print(products)

    return largest



""" Given a position, multiple that num with the right three elements """
def multRight(lists, row, col):
    x=1
    for curr in range(col, col + 4):
        x *= (lists[row][curr])
    return x

""" Given a pos, mult that num with the down three elements """
def multDown(lists, row, col):
    x=1
    for curr in range(row, row + 4):
        x *= (lists[curr][col])
    return x

""" Given a pos, mult that num with the diag down-right 3 elems """
def multDR(lists, row, col):
    x=1
    print("start")
    for curr in range(0, 4):
        x *= (lists[row + curr][col + curr])
        print(row + curr,col + curr)
    return x

""" Given a pos, mult that num with the diag down-left 3 elems """
def multDL(lists, row, col):
    x=1
    print("start")
    for curr in range(0,4):
        x *= (lists[row+ curr][col-curr])
        print(row + curr, col - curr )
    return x



main()