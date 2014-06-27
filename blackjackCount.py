#Shuffle x number of card decks and deal them out by twos, count the number of 21s
import random

cardFaces = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']

decksUsed = 5
deckCount = 0
deck = []
while deckCount < decksUsed:
    for face in cardFaces:
        if face == 'J' or face == 'Q' or face == 'K':
            value = 10
        elif face == 'A':
            value = 11
        else:
            value = face
        deck.append([str(face) + "C", value])
        deck.append([str(face) + "D", value])
        deck.append([str(face) + "H", value])
        deck.append([str(face) + "S", value])
    deckCount += 1
random.shuffle(deck)

totalCount = decksUsed * 52
cardCount = 0
blackjacks = 0
while cardCount < totalCount:
    print deck[cardCount][0] + ' ' + deck[cardCount+1][0]
    if deck[cardCount][1] + deck[cardCount+1][1] ==22:
        deck[cardCount][1] = 1
    totalValue = deck[cardCount][1] + deck[cardCount+1][1]
    print totalValue
    if totalValue == 21:
        blackjacks += 1
    cardCount += 2

hands = totalCount/2
percentBJ = blackjacks/float(hands) * 100
print 'after ' + str(hands) + ' hands there were ' + str(blackjacks) + ' blackjacks at ' + str(int(round(percentBJ))) + '%'


#print deck

#https://docs.python.org/2/library/random.html#random.shuffle
#random.shuffle(x[, random])