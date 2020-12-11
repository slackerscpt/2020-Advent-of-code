def readData():
    with open('input.txt', "r") as read_file:
        inputData = [line.rstrip() for line in read_file]

        return inputData

def readData2():
    with open('input2.txt', "r") as read_file:
        inputData = [line.rstrip() for line in read_file]

        return inputData
def splitAction(action):
    plan, seq = action.split()
    operator = seq[0]
    number = int(seq[1:])

    return plan, operator, number


def setNextPosition(current, direction, number):

    if direction == '-':
        updatedCounter = current - number

    else:
        updatedCounter = current + number

    return updatedCounter


def runItAll(data):
    

    total = len(data)
    counter = 0
    acc = 0
    runCount = 0
    runSeq = []
    highest = 0
    while counter <= total:
        runSeq.append(counter)
        plan, direction, number = splitAction(data[counter])
        if plan == 'jmp':
            print ('Jump')
            print('Updating Jump: %s' %counter)
            counter = setNextPosition(counter, direction, number)
            print('Updating Jump: %s' %counter)
            print ('Number: %s, Direction: %s' %(number, direction))
            print ('Updated Acc: %s' %counter)
        if plan == 'acc':
            acc = setNextPosition(acc, direction, number)
            print (acc)
        if plan == 'nop':
            print ('nop')
            print ('Counter: %s' %counter)
        runCount = runCount + 1
        if plan != 'jmp':
            counter = counter + 1

        if counter > highest:
            highest = counter
        if counter in runSeq:
            print ('breaking do to never ending loop')
            counter = total + 1
            print (counter)

    print (acc)
    print ('Highest: %s' %highest)
    print (runSeq)



def getAcc(data):
    acc = 0
    for lines in data:
        plan, direction, number = splitAction(lines)

        if plan == 'acc':
            acc = setNextPosition(acc, direction, number)
            print (acc)

    print (acc)
runItAll(data = readData())

runItAll(data = readData2())
getAcc(data=readData2())