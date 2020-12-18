def readData():
    with open('input.txt', "r") as read_file:
        inputData = [line.rstrip() for line in read_file]

        return inputData

def part1():
    #eval does not give the correct answer, since order of operations has changed. 
    data = readData()
    total = 0
    for lines in data:
        for values in lines:
            print (values)
        #total += eval(lines)

    #print (total)

part1()