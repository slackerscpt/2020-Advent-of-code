

def findPosition(expNumber, lstNumber):
    last = -1
    for index, number in enumerate(lstNumber):
        if expNumber == number:
            last = index

    return last


def part1():
    numbers = [8,13,1,0,18,9]
    #numbers = [2,1,3]
    counter = len(numbers)
    currentNumber = 0
    while counter < 2020:
        #print ('Turn: %s, number %s' %((counter + 1), currentNumber))
        if currentNumber in numbers:
            lastPosition = findPosition(currentNumber, numbers)
            newNumber = counter - lastPosition
        else:
            newNumber = 0
        numbers.append(currentNumber)
        currentNumber = newNumber
        counter += 1
    print ('Part 1: %s' %numbers[2019])
def part2():
    numbers = [8,13,1,0,18,9]
    #numbers = [2,1,3]
    counter = len(numbers)
    currentNumber = 0
    while counter < 30000000:
        #print ('Turn: %s, number %s' %((counter + 1), currentNumber))
        if currentNumber in numbers:
            lastPosition = findPosition(currentNumber, numbers)
            newNumber = counter - lastPosition
        else:
            newNumber = 0
        numbers.append(currentNumber)
        currentNumber = newNumber
        counter += 1
        

    print ('Part 1: %s' %numbers[30000000])


### more efficent way
def memory_game(input_list, search):
    #This way instead of building a full list of values, it actually builds a dict of numbers and index they last showed at. 
    #indexing from 1, a mortal sin
    d = { num:index for index, num in enumerate(input_list, 1) } 

    #start with the final starting number
    current = input_list[-1]
    index   = len(input_list)

    while index <= search:
        previous   = d.get(current)
        d[current] = index
        current    = index-previous if previous else 0   
        index+=1
    
    #get the key that has the search index as a value
    return list(d.keys())[list(d.values()).index(search)]

part1()
#part2()

numbers = [8,13,1,0,18,9]
p1 = memory_game(numbers, 2020)
p2 = memory_game(numbers, 30000000)

print(f"Part 1 answer: {p1}")
print(f"Part 2 answer: {p2}")