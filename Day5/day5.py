def readData():
    with open('input.txt', "r") as file:
        data = file.read().splitlines()
        return data


def determineSeat():
    data = readData()

    row = 0
    seat = 0
    maxSeatID = 0
    rowValue = 0
    allRows = []
    for rows in data:
        print (rows)
        min = 0
        max = 127
        firstSeven = [0,1,2,3,4,5]
        for numbers in firstSeven:
            range = max - min
            change = (range / 2)
            change = int(change)
            if rows[numbers] == 'F':
                max = min + change
            else:
                min = max - change

        if rows[6] == 'F':
            row = min
        else:
            row = max

        #determine seat number
        seatNumbers = [7,8]
        seatMin = 0
        seatMax = 7
        for numbs in seatNumbers:
            range = seatMax - seatMin
            change = (range / 2)
            change = int(change)
            if rows[numbs] == 'L':
                seatMax = seatMin + change
            else:
                seatMin = seatMax - change
        if rows[9] == 'L':
            seat = seatMin
        else:
            seat = seatMax

        seatId = (row * 8) + seat
        print (seatId)
        allRows.append(seatId)
        if seatId > maxSeatID:
            maxSeatID = seatId
            rowValue = rows

    print ('Max Seat ID: %s' %maxSeatID)
    print('Row: %s' %rowValue)
    allRows.sort()
    print (allRows)

    expectedNumber = 32
    for numbers in allRows:
        print (numbers)
        if expectedNumber == numbers:
            expectedNumber = expectedNumber + 1
        else:
            print('MISSING NUMBER')
    

        



determineSeat()