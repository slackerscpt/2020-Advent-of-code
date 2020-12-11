import copy
currentStatus = {}
previousStatus = {}

def readData():
    with open('input.txt', "r") as read_file:
        inputData = [line.rstrip() for line in read_file]

        return inputData


def setupPreviousStatus():
    global previousStatus
    for rows in currentStatus:
        previousStatus[rows] = {}
        for seats, value in currentStatus[rows].items():
            previousStatus[rows][seats] = value

def setupCurrentStatus():
    data = readData()
    testing = enumerate(data)
    for row, details in testing:
        currentStatus[row] = {}
        seatInfo = enumerate(details)
        for seatNumber, value in seatInfo:
            currentStatus[row][seatNumber]= value


def checkFront(rowNumber, seatNumber):
    occupied = 0
    if rowNumber == 0:
        return occupied
    else:
        current = rowNumber - 1 #don't want to check the current row/seat
        while current >= 0:
            seatCheck = previousStatus[current][seatNumber]
            if seatCheck == "#":
                occupied +=1
                return occupied
            elif seatCheck == "L":
                return occupied
            else:
                current -= 1
        return occupied

def checkBack(rowNumber, seatNumber):
    occupied = 0
    if rowNumber == 93:
        return occupied
    else:
        current = rowNumber + 1
        while current <= 93:
            seatCheck = previousStatus[current][seatNumber]
            if seatCheck == "#":
                occupied += 1
                return occupied
            elif seatCheck == "L":
                return occupied
            else:
                current += 1
        return occupied

def checkRight(rowNumber, seatNumber):
    occupied = 0
    if seatNumber == 91:
        return occupied
    else:
        current = seatNumber + 1
        while current <= 91:
            seatCheck = previousStatus[rowNumber][current]
            if seatCheck == "#":
                occupied += 1
                return occupied
            elif seatCheck == "L":
                return occupied
            else:
                current += 1
        return occupied

def checkLeft(rowNumber, seatNumber):
    occupied = 0
    if seatNumber == 0:
        return occupied
    else:
        current = seatNumber - 1
        while current >= 0:
            seatCheck = previousStatus[rowNumber][current]
            if seatCheck == "#":
                occupied += 1
                return occupied
            elif seatCheck == "L":
                return occupied
            else:
                current -= 1
        return occupied

def checkFrontLeft(rowNumber, seatNumber):
    occupied = 0
    if rowNumber == 0 or seatNumber == 0:
        return occupied
    else:
        currentRow = rowNumber -1 
        currentSeat = seatNumber - 1
        while currentRow >= 0 and currentSeat >= 0:
            seatCheck = previousStatus[currentRow][currentSeat]
            if seatCheck == "#":
                occupied += 1
                return occupied
            elif seatCheck == "L":
                return occupied
            else:
                currentRow -= 1
                currentSeat -= 1
        return occupied

def checkFrontRight(rowNumber, seatNumber):
    occupied = 0
    if rowNumber == 0 or seatNumber == 91:
        return occupied
    else:
        currentRow = rowNumber -1 
        currentSeat = seatNumber + 1
        while currentRow >= 0 and currentSeat <= 91:
            seatCheck = previousStatus[currentRow][currentSeat]
            if seatCheck == "#":
                occupied += 1
                return occupied
            elif seatCheck == "L":
                return occupied
            else:
                currentRow -= 1
                currentSeat += 1
        return occupied

def checkBackLeft(rowNumber, seatNumber):
    occupied = 0
    if rowNumber == 93 or seatNumber == 0:
        return occupied
    else:
        currentRow = rowNumber +1 
        currentSeat = seatNumber - 1
        while currentRow <= 93 and currentSeat >= 0:
            seatCheck = previousStatus[currentRow][currentSeat]
            if seatCheck == "#":
                occupied += 1
                return occupied
            elif seatCheck == "L":
                return occupied
            else:
                currentRow += 1
                currentSeat -= 1
        return occupied

def checkBackRight(rowNumber, seatNumber):
    occupied = 0
    if rowNumber == 93 or seatNumber == 91:
        return occupied
    else:
        currentRow = rowNumber +1 
        currentSeat = seatNumber + 1
        while currentRow <= 93 and currentRow <= 91:
            seatCheck = previousStatus[currentRow][currentSeat]
            if seatCheck == "#":
                occupied += 1
                return occupied
            elif seatCheck == "L":
                return occupied
            else:
                currentRow += 1
                currentSeat -= 1
        return occupied
   
            
def checkAdjacentSeats(rowNumber, seatNumber):
    #All decisions are based on the number of occupied seats adjacent to a given seat (one of the eight positions immediately up, down, left, right, or diagonal from the seat)
    # 123
    # 4X6
    # 789
    # We will count the number of seats occupied and return the count
    # We need to have some catches
    # For Row 0 we can't check row ahead
    # For Row 93 we can't check row behind
    # For Seat 0 we can't check seat to the left of it
    # For Seat 91 we can't check seat to the right of it. 

    rowstoCheck = [rowNumber -1, rowNumber, rowNumber + 1]
    seatsToCheck = [seatNumber -1, seatNumber, seatNumber + 1]
    if rowNumber == 0:
        rowstoCheck.pop(0)
    if rowNumber == 93:
        rowstoCheck.pop(2)
    if seatNumber == 0:
        seatsToCheck.pop(0)
    if seatNumber == 91: 
        seatsToCheck.pop(2)
    
    #we have our row and seats to check
    occupiedSeats = 0
    for rows in rowstoCheck:
        for seats in seatsToCheck:
            if rows == rowNumber and seats == seatNumber:
                continue
            seatCheck = previousStatus[rows][seats]
            if seatCheck == "#":
                occupiedSeats += 1

    return occupiedSeats


def setCurrentSeats(previousOccupiedSeats):
    changedSeats = 0
    totalOccupiedSeats = 0
    for rows in currentStatus:
        for seats, value in currentStatus[rows].items():
            if value == ".":
                continue
            seatsTaken = checkAdjacentSeats(rows, seats)
            if seatsTaken == 0:
                updatedValue = "#"
            elif seatsTaken >= 4:
                updatedValue = "L"
            else:
                updatedValue = value
            if updatedValue == "#":
                totalOccupiedSeats += 1
            #Lets update the value
            if updatedValue != value:
                changedSeats += 1
            currentStatus[rows][seats] = updatedValue

    if changedSeats != 0:
        #Let's update previous
        setupPreviousStatus()

    if previousOccupiedSeats == totalOccupiedSeats:
        print('Part 1: Total Seats stagnet at: %s' %totalOccupiedSeats)
        return 0, totalOccupiedSeats
    return changedSeats, totalOccupiedSeats 


def checkSeatsPart2(rows, seats):
    front = checkFront(rows, seats)
    back = checkBack(rows, seats)
    right = checkRight(rows, seats)
    left = checkLeft(rows, seats)
    frontLeft = checkFrontLeft(rows, seats)
    frontRight = checkFrontRight(rows, seats)
    backLeft = checkBackLeft(rows, seats)
    backRight = checkBackRight(rows, seats)
    totalSeats = front + back + right + left + frontLeft + frontRight + backLeft + backRight
    
    return totalSeats

def part2Seats(takenSeats):
    changedSeats = 0
    totalOccupiedSeats = 0
    for rows in currentStatus:
        for seats, value in currentStatus[rows].items():
            if value == ".":
                continue
            totalSeats = checkSeatsPart2(rows, seats)
            if totalSeats == 0:
                updatedValue = "#"
            elif totalSeats >= 5:
                updatedValue = "L"
            else:
                updatedValue = value

            if updatedValue == "#":
                totalOccupiedSeats += 1

            if updatedValue != value:
                changedSeats += 1
            currentStatus[rows][seats] = updatedValue

    if changedSeats != 0:
        #Let's update previous
        setupPreviousStatus()
    if takenSeats == totalOccupiedSeats:
        print('Part 2: Total Seats stagnet at: %s' %totalOccupiedSeats)
        return 0, totalOccupiedSeats
    return changedSeats, totalOccupiedSeats 

def part1():
    setupCurrentStatus()
    setupPreviousStatus()
    changedSeats, totalSeats = setCurrentSeats(0)
    while changedSeats > 0:
        changedSeats, totalSeats = setCurrentSeats(totalSeats)

def part2():
    setupCurrentStatus()
    setupPreviousStatus()
    changedSeats, totalSeats = part2Seats(0)
    while changedSeats > 0:
        changedSeats, totalSeats = part2Seats(totalSeats)

part1()
part2()


