import re

blank_line_regex = r"(?:\r?\n){2,}"

def readData():
    with open('input.txt', "r") as file:
        data2 = file.read()
        updatedData = re.split(blank_line_regex, data2.strip())

    return updatedData


def checkAnswers():
    data = readData()
    overallLeters = []

    for groups in data:
        dataGroup = []
        lineGroup = ''
        groupData = groups.splitlines()
        for lines in groupData:
            dataGroup.append(lines)
            lineGroup = lineGroup + lines
        
        countOfLetters = checkDuplicates(lineGroup)
        overallLeters.append(countOfLetters)

    return overallLeters

def checkDuplicates(line):
    letters = []
    for chars in line:
        if chars not in letters:
            letters.append(chars)

    uniqLetters = len(letters)
    return uniqLetters
        
def countLetters(countOfLetters):
    value = 0
    for numbers in countOfLetters:
        value = numbers + value

    print ('Part1 Value: %s' %value)

def countAnswers(data, numberofPeople):
    #data is a single line
    letters = []

    for chars in data:
        counter = 0
        for letter in data:
            if chars == letter:
                counter = counter + 1

        if counter == numberofPeople:
            if chars not in letters:
                letters.append(chars)

    return (len(letters))
def part2():
    data = readData()
    overallLetters = []
    for lines in data:
        
        lineGroup = ''
        groupData = lines.splitlines()
        numberOfPeople = len(groupData)
        for lines in groupData:
            lineGroup = lineGroup + lines


        counter = countAnswers(lineGroup, numberOfPeople)
        overallLetters.append(counter)

    return overallLetters

countOfLetters = checkAnswers()
countLetters(countOfLetters)
lettersPart2 = part2()
countLetters(lettersPart2)
