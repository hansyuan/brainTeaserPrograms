# read the file
# add all the digits together 
# print the first ten digits of that sum

fileName = "small"
fileName = fileName + ".txt"
file = open(fileName, "r")
sum = 0
while True:
    eachLine = file.readline()
    if len(eachLine) == 0: break
    eachLine = int(eachLine.replace('\n',""))
    sum += eachLine

print (sum)