def readData():
    with open('input.txt', "r") as read_file:
        inputData = [line.rstrip() for line in read_file]

        return inputData


def deconstructData(data):
        validPassword = 0
        for items in data:
            [pwRange, pwLetter, pwValue] = items.split()
            [minRange,maxRange] = pwRange.split('-')
            [updatedLetter, null] = pwLetter.split(':')
            minRangeInt = int(minRange)
            maxRangeInt = int(maxRange)

            count = 0

            for i in pwValue:
                if i == updatedLetter:
                    count = count + 1

            if minRangeInt <= count <= maxRangeInt:
                validPassword = validPassword + 1

        print ("Total Valid Passwords Part 1: %s" %validPassword)

def part2(data):
        validPassword = 0
        for items in data:
            [pwRange, pwLetter, pwValue] = items.split()
            [minRange,maxRange] = pwRange.split('-')
            [updatedLetter, null] = pwLetter.split(':')
            minRangeInt = int(minRange) - 1
            maxRangeInt = int(maxRange) - 1
            count = 0
            if (pwValue[minRangeInt] == updatedLetter):
                count = count + 1
            if (pwValue[maxRangeInt] == updatedLetter):
                count = count + 1

            if count == 1:
                validPassword = validPassword + 1

        print ("Total Valid Passwords Part 2: %s" %validPassword) 


data = readData()
deconstructData(data)
part2(data)
