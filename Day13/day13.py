from sympy.ntheory.modular import crt

def readData():
    with open('input.txt', "r") as read_file:
        inputData = [line.rstrip() for line in read_file]

        return inputData

def determineTimeDiff(timeStamp, busNumber):

    nextBusTime = timeStamp / busNumber
    nextBusTime = int(nextBusTime) + 1
    timing = nextBusTime * busNumber
    waitTime = timing - timeStamp

    return (waitTime, (waitTime * busNumber))

def busSchedule():
    buses = {}
    fatestWaitTime = 34343243242342343243424234234234324234234324234
    fastBus = 0
    data = readData()
    timeStamp = int(data[0])
    busTiming = data[1].split(',')
    for times in busTiming:
        if times != 'x':
            
            #print (times,busTiming.index(times))
            intTimes = int(times)
            waitTime, product = determineTimeDiff(timeStamp, intTimes)
            buses[times] = []
            buses[times].append([waitTime, product])
            if waitTime < fatestWaitTime:
                fatestWaitTime = waitTime
                fastBus = times

    print ('Fastest Bus is %s' %fastBus)
    print ('Wait Time, Product: %s' %buses[fastBus])


    #print (busTiming)

def part2():

    #googling pointed me to Chinese Remainder Theorem, which is crt
    data = readData()
    modulos = []
    remainders = []

    busTimestamps = data[1].split(",")
    for i in range(len(busTimestamps)):
        if busTimestamps[i].isnumeric():
            modulos.append(int(busTimestamps[i]))
            remainders.append((-i) % modulos[-1])

    print(modulos)
    print(remainders)

    ans = crt(modulos, remainders)

    print(ans)


busSchedule()
part2()