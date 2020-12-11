def readData():
    with open('input.txt', "r") as read_file:
        inputData = [line.rstrip() for line in read_file]

        return inputData


def checkIfCanAddUp(number, otherNumbers):
    for numbers in otherNumbers:
        combo = number - numbers
        #print ('Looking for %s' %combo)
        if combo in otherNumbers:
            return True
    
    return False


def addUpNumbers(number, otherNumbers):
    total = number
    for numbers in otherNumbers:
        total += numbers

    return total

def doubleCheck(numbers):
    total = 0
    for count in numbers:
        total += count

    return total

def runData():
    data = readData()
    activeNumbers = []
    counter = 0
    for numbers in data:
        numbers = int(numbers)
        if counter <= 24:
            activeNumbers.append(numbers)
            counter += 1
        else:            
            check = checkIfCanAddUp(numbers, activeNumbers)
            del activeNumbers[:0]
            activeNumbers.append(numbers)
            #print(numbers, check)

            if not check:
                print ('Part 1 Answer: %s' %numbers)
                break

def part2():
    target = 20874512
    data = readData()
    newData = []
    for numbers in readData():
        newData.append(int(numbers))
    sums = set()
    for i in range(len(newData)):
        if (target - newData[i]) in sums:
            group, sum = [], 0
            for j in range(i):
                group.append(newData[i-j])
                sum += newData[i-j]
                if sum == target:
                    return min(group) + max(group)

        else:
            newSums = set()
            for number in sums:
                newSums.add(number + newData[i])
            newSums.add(newData[i])
            sums = newSums

    return "Invalid"



runData()
answer = part2()
print('Part 2 Answer: %s' %answer)