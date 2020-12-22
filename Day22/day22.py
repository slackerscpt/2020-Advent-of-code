import re
def readData():
    with open('input.txt', "r") as read_file:
        inputData = [line.rstrip() for line in read_file]
    return inputData


def buildPlayersDecks():
    data = readData()
    deck = {}
    setPlayer = None
    for info in data:
        if 'Player' in info:
            setPlayer = info[:-1]
            deck[setPlayer] = []
        else:
            if '' != info:
                deck[setPlayer].append(int(info))


    return deck

def playGame(deck):
    #We start with each player having 25 cards
    roundNumber = 1
    while (len(deck['Player 1']) > 0 and len(deck['Player 2']) > 0):
        print ('--Round Number %s' %roundNumber)
        print ('Player 1 deck: %s' %deck['Player 1'])
        print ('Player 2 deck: %s' %deck['Player 2'])
        print ('Player 1 plays: %s' %deck['Player 1'][0])
        print ('Player 2 plays: %s' %deck['Player 2'][0])
        if deck['Player 1'][0] > deck['Player 2'][0]:
            print ('Player 1 Wins')
            deck['Player 1'].append(deck['Player 1'][0])
            deck['Player 1'].append(deck['Player 2'][0])
            deck['Player 1'].pop(0) #We need to remove to played card
            deck['Player 2'].pop(0)

        else:
            print ('Player 2 Wins')
            deck['Player 2'].append(deck['Player 2'][0])
            deck['Player 2'].append(deck['Player 1'][0])
            deck['Player 1'].pop(0) #We need to remove to played card
            deck['Player 2'].pop(0)

        roundNumber += 1
        
    return deck

def totalWinner (cards, totalSum):
    multipler = len(cards)
    for valueOfCard in cards:
        totalSum += (valueOfCard * multipler)
        multipler -= 1

    return totalSum

def part1Winner(deck):
    totalSum = 0
    for keys in deck:
        if len(deck[keys]) > 0:
            totalSum = totalWinner(deck[keys], totalSum)

    print ('Part 1 Answer: %s' %totalSum)

if __name__ == "__main__":
    setDeck = buildPlayersDecks()
    playedDeck = playGame(setDeck)
    part1Winner(playedDeck)