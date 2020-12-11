def readData():
    with open('input.txt', "r") as read_file:
        inputData = [line.rstrip() for line in read_file]

        return inputData

def find_shiny_gold(bagMap, bag):
    for _, next_bag in bagMap[bag]:
        if next_bag == "shiny gold" or find_shiny_gold(bagMap, next_bag):
            return True
    return False


def countBags(bagMap, bag):
    return sum(bag_count * ( 1 + countBags(bagMap, next_bag)) for bag_count, next_bag in bagMap[bag])
    
def generatMapping():
    data = readData()
    bagMapping = {}
    for bags in data:
        extraBags  = []
        carryBag, otherBags = bags.split(" bags contain ")
        others = otherBags.rstrip(".\n").split(", ")
        for moreBags in others:
            if moreBags != "no other bags":
                extraInfo = moreBags.split(" ")
                number = int(extraInfo[0])
                bagInfo = " ".join(extraInfo[1:-1])
                #print (bagInfo)
                extraBags.append((number, bagInfo))
        bagMapping[carryBag] = extraBags

    return bagMapping


bagMap = generatMapping()
result = sum(find_shiny_gold(bagMap, bag) for bag in bagMap.keys())
print ('Part 1: %s' %result)

result2 = countBags(bagMap, "shiny gold")
print ('Part 2: %s' %result2)