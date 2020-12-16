import re
def readData():
    with open('nearby.txt', "r") as read_file:
        inputData = [line.rstrip() for line in read_file]

        return inputData

def readDatap2():
    with open('input.txt', "r") as read_file:
        inputData = [line.rstrip() for line in read_file]

        return inputData

def part1():
    data = readData()
    captures = []
    for lines in data:
        numbers = lines.split(',')
        for values in numbers:
            if 25<= int(values) <= 974:
                continue
            else:
                captures.append(int(values))

    total = sum(captures)
    print ('Part 1: %s' %total)

def redfineData(lineHolders):
    ticketRows = {}
    myTicket = []
    nearbyTickets = []
    for keys in lineHolders:
        values = keys.split(':')
        if values[1]:
            ticketRows[values[0]] = {}
            range1, range2 = values[1].split(' or ')
            range1Min, range1Max = range1.split('-')
            range2Min, range2Max = range2.split('-')
            ticketRows[values[0]]['range1Min'] = int(range1Min)
            ticketRows[values[0]]['range1Max'] = int(range1Max)
            ticketRows[values[0]]['range2Min'] = int(range2Min)
            ticketRows[values[0]]['range2Max'] = int(range2Max)
        else:
            if (values[0] == 'your ticket'):
                ticketNumber = lineHolders[keys][0].split(',')
                for numbers in ticketNumber:
                    myTicket.append(int(numbers))
            else:
                nearbyTickets = lineHolders[keys]

    return ticketRows, myTicket, nearbyTickets


def clearUpNearbyTickets(nearbyTickets):
    updatedTickets = []

    for tickets in nearbyTickets:
        numbers = tickets.split(',')
        valid = True
        for values in numbers:
            if 25<= int(values) <= 974:
                continue
            else:
                valid = False
        if valid:
            updatedTickets.append(tickets)

    return updatedTickets

def validateLocation(rangeValues, nearbyTickets):
    invalidPosition = []
    for tickets in nearbyTickets:
        ticketNumbers = tickets.split(',')
        for numbers in ticketNumbers:
            if (rangeValues['range1Min'] <= int(numbers) <= rangeValues['range1Max']) or (rangeValues['range2Min'] <= int(numbers) <= rangeValues['range2Max']):
                continue
            else:
                #we have a number that does not fit the range
                invalidPosition.append(ticketNumbers.index(numbers))

    return invalidPosition

def validNumbers(invalidList):
    validPositions = []
    counter = 0
    while counter < 20:
        if counter not in invalidList:
            validPositions.append(counter)
        counter += 1

    return validPositions


def determineAssignment(ticketInfo):
    #need to handle deleting keys
    #Need to go through each item, 
    assignedValues = {}
    numbersTaken = []
    while len(numbersTaken) < 20:
        for keys in ticketInfo:
            if len(ticketInfo[keys]) == 1:
                assignedValues[keys] = ticketInfo[keys][0]
                numbersTaken.append(ticketInfo[keys][0])
                #ticketInfo.pop(keys, None) #remove the key from the dict
            else:
                for numbers in numbersTaken:    
                    if numbers in ticketInfo[keys]:
                        ticketInfo[keys].remove(numbers)
        for keys in assignedValues:
            if keys in ticketInfo:
                del ticketInfo[keys]
    return assignedValues


def part2():
    data = readDatap2()
    lineHolders = {}
    keyValue = False
    for lines in data:
        if re.match("^[a-zA-Z]+.*", lines):
            keyValue = lines
            lineHolders[keyValue] = []
        else:
            lineHolders[keyValue].append(lines)

    #let's clean up the data
    ticketRows, myTicket, nearbyTickets = redfineData(lineHolders)
    updatedTickets = clearUpNearbyTickets(nearbyTickets)

    availableRows = {}
    for ticketInfo in ticketRows:
        invalidPositions = validateLocation(ticketRows[ticketInfo], updatedTickets)
        validPositions = validNumbers(invalidPositions)
        availableRows[ticketInfo] = []
        availableRows[ticketInfo] = validPositions

    assignedRows = determineAssignment(availableRows)
    number = 1
    for rows in assignedRows:
        if 'departure' in rows:
            number *= myTicket[assignedRows[rows]]

    print ('Part 2: %s' %number)

part1()
part2()