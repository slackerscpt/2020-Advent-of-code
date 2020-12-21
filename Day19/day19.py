import re
def readData():
    with open('input.txt', "r") as read_file:
    #with open('test.txt', "r") as read_file:
    #with open('test2.txt', "r") as read_file:
        inputData = [line.rstrip() for line in read_file]

        return inputData


def updateRules(rules, updates):
    print ('Running updates')
    for update in updates:
        value = updates[update]
        for keys, values in rules.items():
            print (values)
            if str(update) in values:
                rules[keys] = re.sub(str(update), value, values)

    print (rules)

    determineUpdate(rules)

def determineUpdate(rules):
    updates = {}
    for rule, ruleValues in rules.items():
        print (rule, ruleValues)
        if not (bool(re.search(r'\d', ruleValues))):
            updates[rule] = ruleValues

    if updates:
        updateRules(rules, updates)
def buildRules(rules):
    ruleBook = {}
    updates = {}
    for rule in rules:
        if ":" in rule:
            ruleNumber, notes = rule.split(': ')
            ruleNumber = int(ruleNumber)
            
            if '"' in notes:
                updates[ruleNumber] = notes[1]
                ruleBook[ruleNumber] = notes[1]
            else:
                ruleBook[ruleNumber] = notes

    updateRules(ruleBook, updates)

    return ruleBook
            
def getRules(ruleNumber, ruleBook):
    ruleNumber = int(ruleNumber)
    newRules = ruleBook[ruleNumber].split()
    print (newRules)

def part1():
    data = readData()
    letters = ('a', 'b')
    messages = []
    rules = []
    for lines in data:
        if lines.startswith(letters):
            messages.append(lines)
        else:
            rules.append(lines)

    ruleBook = buildRules(rules)
    print (ruleBook[0])
    numbers = ruleBook[0].split()
    for number in numbers:
        getRules(number, ruleBook)


part1()