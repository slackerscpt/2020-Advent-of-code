
def readData():
    with open('input.txt', "r") as read_file:
        inputData = [int(line.rstrip()) for line in read_file]
    return inputData


def part1():
    data = readData()
    for items in data:
        neededValue = 2020 - items
        #print (neededValue)

        if neededValue in data:
            print ('1: %s' %neededValue)
            print ('2 %s' %items)
            print ('Result: %s' %(items * neededValue) )
            return


def part2():
    # Looking for 3 numbers that equal 2020
    data = readData()
    for numbers in data:
        for num2 in data:
            if numbers != num2:
                current = numbers + num2
                if 2020 > current:
                    needed = 2020 - current
                    if needed in data:
                        print ('1: %s' %numbers)
                        print ('2: %s' %num2)
                        print ('3: %s' %needed)
                        total = numbers * num2 * needed
                        print('Result: %s' %total)
                        return
            
    

part1()
part2()
    