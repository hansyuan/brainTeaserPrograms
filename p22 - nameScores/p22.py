


def readNamesAsList():
    file = open ("names.txt",'r')
    s = file.readline().replace('"','').split(",")
    s.sort()
    return s

def totalScore(s):
    retScore = 0
    rank = 0
    for x in s:
        rank += 1
        sum = 0
        for ch in x:
            sum += score[ch]
        retScore += sum * rank
    return retScore


score = {}
for chs in range(65,91):
     score[chr(chs)] = chs - 64


l = readNamesAsList()
s = totalScore(l)

print (s)