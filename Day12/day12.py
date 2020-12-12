debug = False
def readData():
    with open('input.txt', "r") as read_file:
    #with open('test.txt', "r") as read_file:
    #with open('test2.txt', "r") as read_file:
        inputData = [line.rstrip() for line in read_file]

        return inputData



def setupData() :
    data = readData()
    updatedData = []
    for numbers in data:
        direction = numbers[0]
        num = numbers[1:]
        num = int(num)
        updatedData.append([direction, num])

    return updatedData


def changeDirection(currentDirection, newChange, changePercent):
    allDirections = ['N', 'E', 'S', 'W']
    allChanges = [0, 90, 180, 270]
    changeNumber = allDirections.index(currentDirection)
    rotationChange = allChanges.index(changePercent)

    if newChange == 'R':
        newChangeNumber = rotationChange + changeNumber
        if newChangeNumber > 3:
            newChangeNumber -= 4
    if newChange == 'L':
        newChangeNumber = changeNumber - rotationChange
        if newChangeNumber < 0:
            newChangeNumber += 4


    return allDirections[newChangeNumber]

def changeDirectionP2(currentDirection, newChange, changePercent, NS, EW):
    allDirections = ['N', 'E', 'S', 'W']
    allChanges = [0, 90, 180, 270]
    changeNumber = allDirections.index(currentDirection)
    rotationChange = allChanges.index(changePercent)

    if newChange == 'R':
        newChangeNumber = rotationChange + changeNumber
        if newChangeNumber > 3:
            newChangeNumber -= 4
        if rotationChange == 1: 
            NS,EW = -EW,NS
            
        elif rotationChange == 3:
            NS,EW = EW,-NS
        
    if newChange == 'L':
        newChangeNumber = changeNumber - rotationChange
        if newChangeNumber < 0:
            newChangeNumber += 4
        if rotationChange == 1: 
            NS,EW = EW,-NS
        elif rotationChange == 3:
            NS,EW = -EW,NS

    if rotationChange == 2:
        NS,EW = -NS,-EW

    return (allDirections[newChangeNumber], NS, EW)




def part1():
    shipDirections = setupData()
    currentDirection = 'E'
    EWNumber = 0
    NSNumber = 0

    for direction, dirValue in shipDirections:
        if direction == 'F':
            if currentDirection == 'E':
                EWNumber += dirValue
            elif currentDirection == "W":
                EWNumber -= dirValue
            elif currentDirection == 'S':
                NSNumber -= dirValue
            else:
                NSNumber += dirValue
        if direction == 'E':
            EWNumber += dirValue
        if direction == 'W':
            EWNumber-= dirValue
        if direction == 'S':
            NSNumber -= dirValue
        if direction == 'N':
            NSNumber += dirValue

        if direction == 'R' or direction == 'L':
            currentDirection = changeDirection(currentDirection, direction, dirValue)

    print ('Part 1 Answer: %s' %(abs(NSNumber) + abs(EWNumber)))


def part2():
    shipDirections = setupData()
    currentDirection = 'E'
    EWNumber = 0
    NSNumber = 0
    wayPointN = 1
    wayPointE = 10

    for direction, dirValue in shipDirections:

        if direction == 'F':
            updateN = wayPointN * dirValue
            updateE = wayPointE * dirValue
            # if currentDirection == 'E' or currentDirection == 'W':
            #     updateN = wayPointN * dirValue
            #     updateE = wayPointE * dirValue
            # else:
            #     updateN = wayPointE * dirValue
            #     updateE = wayPointN * dirValue

            # if currentDirection == 'S':
            #     updateN = 0 - updateN
            # if currentDirection == 'W':
            #    updateE = 0 - updateE
            NSNumber += updateN
            EWNumber += updateE
        if direction == 'E':
            wayPointE += dirValue
        if direction == 'W':
            wayPointE -= dirValue
        if direction == 'S':
            wayPointN -= dirValue
        if direction == 'N':
            wayPointN += dirValue

        if direction == 'R' or direction == 'L':
            currentDirection, wayPointN, wayPointE = changeDirectionP2(currentDirection, direction, dirValue, wayPointN, wayPointE)
            #currentDirection = changeDirection(currentDirection, direction, dirValue)
        if debug:
            print('---')
            print (direction, dirValue)
            print('EW: %s' %wayPointE)
            print('NS; %s' %wayPointN)
            print ('East: %s' %EWNumber)
            print ('North: %s' %NSNumber)
            print (currentDirection)

    print ('Part 2 Answer: %s' %(abs(NSNumber) + abs(EWNumber)))

part1()
part2()
