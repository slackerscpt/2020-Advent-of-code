from collections import Counter

def readData():
    with open('input.txt', "r") as read_file:
        inputData = [int(line.rstrip()) for line in read_file]

        inputData.append(0)
        inputData.append(max(inputData) + 3)

        return inputData

def runData():
    numbers = readData()
    numbers.sort()
    data = Counter([numbers[i] - numbers[i-1] for i in range(1, len(numbers))])
    print ('Part 1: %s' %(data[1] * data[3]))

def count_ways(A, ht):
    if len(A) == 1:
        return 1
    if A[0] not in ht:
        ht[A[0]] = sum(count_ways(A[i:], ht) for i, x in enumerate(A[1:4], 1) if x - A[0] < 4)
    return ht[A[0]]

runData()
data = readData()
data.sort()
result = count_ways(data, {})
print ('Part 2: %s' %result)


