# max path sum

def buildTree():
    small = "small.txt"
    normal = "test.txt"
    med = "medium.txt"
    
    file = open(normal,"r")
    ret = []
    levels = 0

    # Continually read the inputs from the tree. 
    # Each line should have twice as many elems as the prev. 
    while True:
        levels += 1
        currLine = file.readline().replace('\n',"")
        if len (currLine) == 0: break
        currLine = [int(x) for x in currLine.split(" ")]
        for x in currLine:
            ret.append(x)
    return ret, levels
        



def getChildren(tree, position, height):
    left = position + height
    right = position + height + 1
    return left, tree[left], right, tree[right]

#recursively traverse, return list of values that results in largest total
def buildPath(tree, position, height, pathValue, heightMax):


    # if base case, return list of lists
    if height == 1:


    # if recursive case, will get 2 lists. add to both, then return both

    # if last case, create a list and add the last element and return it
    return list()


#given a position in the tree, returns the position and val of the bigger child
def getMaxChildValAndPos(tree, position, height):
    left, lval, right, rval = getChildren(tree, position, height)
    if lval < rval:
        return right, rval
    else: 
        return left, lval

def main():
    tree, heightMax = buildTree()
    position = 0    # root of the tree
    height = 1      # next height, not current height
    value = tree[position]

    path = []
    path.append(value)



    while height < heightMax - 1:
        position, value = getMaxChildValAndPos(tree, position, height)
        path.append(value)
        height += 1

    return (path)

main()