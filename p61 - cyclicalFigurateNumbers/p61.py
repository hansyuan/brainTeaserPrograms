def tri(n):
    return int(n * (n+1) / 2)
def squ(n):
    return int(n**2)
def pen(n):
    return int(n*(3*n-1)/2)
def hxa(n):
    return int(n*(2*n-1))
def hep(n):
    return int(n*(5*n-3)/2)
def ota(n):
    return int(n*(3*n-2))

def check(li):
    
    for x in range(0,5):
        
        if li[x][2]+li[x][3] != li[x+1][0] + li[x+1][1]:
            return False
    return li[5][2]+li[5][3] == li[0][0] + li[0][1]

def check(num, num2):
    return num[2]+num[3] == num2[0] + num2[1]

""" There has got to be a better way of writing this """

def main():
    # consider all 4 digit nums
    max = 9000
    min = 999

    tri1 = [ str(tri(n)) for n in range(1,300) if tri(n) < max and tri(n) > 999]
    squ1 = [ str(squ(n)) for n in range(1,300) if squ(n) < max and squ(n) > 999]
    pen1 = [ str(pen(n)) for n in range(1,300) if pen(n) < max and pen(n) > 999]
    hxa1 = [ str(hxa(n)) for n in range(1,300) if hxa(n) < max and hxa(n) > 999]
    hep1 = [ str(hep(n)) for n in range(1,300) if hep(n) < max and hep(n) > 999]
    ota1 = [ str(ota(n)) for n in range(1,300) if ota(n) < max and ota(n) > 999]
    empty = "empty"


    # algorithm: BFS
    # from the first set, pick a 4 digit number
    #   in the next set, find a num with 1st 2 digs matching first num's last 2
    #   keep going to the next set, doing the same thing until reaching the 6th set
    #   by which, compare with the num from the first set. 
    #   if not found, exhaust the 6th set inner out.

    # note: there are 6 sets to choose from to be the 1st set, then 5, and so on..

    shapes = {}
    shapes[0] = tri1
    shapes[1] = squ1
    shapes[2] = pen1
    shapes[3] = hxa1
    shapes[4] = hep1
    shapes[5] = ota1






    comps = 0

    for first in range(0,6):
        firstSet = shapes[first]
        shapes[first] = empty
        #break #comment out when not testing
        for firstNum in firstSet:
            #print (firstNum)
            

            for second in range(0,6):
                secSet = shapes[second]
                if secSet == empty: continue
                shapes[second] = empty
                for secondNum in secSet:
                    if not check(firstNum,secondNum):
                        continue

                
                    for third in range(0,6):
                        thiSet = shapes[third]
                        if thiSet == empty: continue
                        shapes[third] = empty
                        for thirdNum in thiSet:
                            if not check(secondNum, thirdNum):
                                continue
                        
                            for fourth in range(0,6):
                                fouSet = shapes[fourth]
                                if fouSet == empty: continue
                                shapes[fourth] = empty
                                for fourthNum in fouSet:
                                    if not check(thirdNum, fourthNum):
                                        continue

                                    for fifth in range(0,6):
                                        fifSet = shapes[fifth]
                                        if fifSet == empty: continue
                                        shapes[fifth] = empty
                                        for fifthNum in fifSet:
                                            if not check(fourthNum, fifthNum):
                                                continue
                                        
                                            for sixth in range(0,6):
                                                sixSet = shapes[sixth]
                                                if sixSet == empty: continue
                                                shapes[sixth] = empty
                                                for sixthNum in sixSet:
                                                    if not check(fifthNum,sixthNum):
                                                        continue
                                                    else:
                                                        if check(sixthNum, firstNum):
                                                            print(
                                                                first,
                                                                second,
                                                                third,
                                                                fourth,
                                                                fifth,
                                                                sixth
                                                                )
                                                            print(
                                                                "FOUND:",
                                                                firstNum,
                                                                secondNum,
                                                                thirdNum,
                                                                fourthNum,
                                                                fifthNum,
                                                                sixthNum)
                                                            print(int(firstNum)
                                                                +
                                                                int(secondNum)
                                                                +
                                                                int(thirdNum)
                                                                +
                                                                int(fourthNum)
                                                                +
                                                                int(fifthNum)
                                                                +
                                                                int(sixthNum))
                                                            return
                                                    comps+=1
                                                    
                                                    

                                                shapes[sixth] = sixSet
                                        shapes[fifth] = fifSet
                                shapes[fourth] = fouSet
                        shapes[third] = thiSet
                shapes[second] = secSet
        shapes[first] = firstSet
    print (comps)

main()