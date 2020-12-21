import re
def readData():
    with open('input.txt', "r") as read_file:
        inputData = [line.rstrip() for line in read_file]
    return inputData


def part1():
    menu = readData()
    listOfAllergens = {}
    allIngreds = []
    for items in menu:
        ingredients, allergens = items.split('(contains ')
        for item in ingredients.split():
            allIngreds.append(item)
        if "," in allergens:
            for allergen in allergens[:-1].split(', '):
                if allergen not in listOfAllergens:
                    listOfAllergens[allergen] = []
                listOfAllergens[allergen].append(set([item for item in ingredients.split()]))
        else:
            if allergens[:-1] not in listOfAllergens:
                listOfAllergens[allergens[:-1]] = []
            listOfAllergens[allergens[:-1]].append(set([item for item in ingredients.split()]))


    #we have each item setup by allergen now. 
    #we should see what value is common in each. 
    fullAllergens = {}
    for keys, values in listOfAllergens.items():
        possibleIntersection = set.intersection(*values)
        fullAllergens[keys] = possibleIntersection

    allergenInd = []
    for allergens in fullAllergens:
        for items in fullAllergens[allergens]:
            if items not in allergenInd:
                allergenInd.append(items)

    counter = 0
    for item in allIngreds:
        if item not in allergenInd:
            counter += 1

    print ('Part 1 Answer: %s' %counter)
    part2(fullAllergens)



def part2(fullAllergens):
    #we have 7 allergines, but multiple in each. 
    definedAllergy = {}
    values2Remove = []
    keysFound = []
    while len(keysFound) < 7:
        for allergy in sorted(fullAllergens):
            if allergy not in definedAllergy:
                currentvalues = fullAllergens[allergy]
                for foundValues in values2Remove:
                    if foundValues in currentvalues:
                        currentvalues.remove(foundValues)
                fullAllergens[allergy] = currentvalues
                if (len(fullAllergens[allergy])) == 1:
                    definedAllergy[allergy] = fullAllergens[allergy]
                    for item in fullAllergens[allergy]:
                        #since we put them in sets, we need to unpack it. 
                        #Not using loop would put it as a set
                        values2Remove.append(item)
                    keysFound.append(allergy)

    allergen_foods = ','.join([list(definedAllergy[key])[0] for key in sorted(definedAllergy)])
    print(f"Part 2 Answer: {allergen_foods}")



part1()