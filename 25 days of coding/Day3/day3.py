def readData():
    with open('input.txt', "r") as read_file:
        inputData = [line.rstrip() for line in read_file]

        return inputData


def slopeRun(slopeData, shift):
    position = 0
    trees = 0
    for lines in slopeData:

        if lines[position] == '#':
            trees = trees + 1

        position = position + shift
        if (position > 30):
            position = position - 31

    return trees

def slopeRunEven(slopeData, shift):
    counter = 0
    trees = 0
    position = 0
    for lines in slopeData:
        if (counter % 2) == 0:
            if lines[position] == '#':
                trees = trees + 1
                

            position = position + shift
            if (position > 30):
                position = position - 31 
        counter = counter + 1
    return trees
    

def part1():
    slopeData = readData()
    results = slopeRun(slopeData, 3)
    print('Total Trees hit (part1): %s' %results)


def part2():
    slopeData = readData()
    totalTrees = []
    newTrees = []
    rightNumbers = [1, 3, 5, 7]
    for right in rightNumbers:
        totalTrees.append(slopeRun(slopeData, right))
    totalTrees.append(slopeRunEven(slopeData, 1))
    sumTrees = 1
    for numbers in totalTrees:
        sumTrees *= numbers

    print ('Part 2 Total: %s' %sumTrees)

part1()
part2()