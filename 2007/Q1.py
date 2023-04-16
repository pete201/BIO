'''https://www.olympiad.org.uk/papers/2007/bio/round_one.html'''

debug = False

def rule1(deck):
    '''iterarion. a point for all combinations of identical numerical values'''
    points = 0
    for index,value in enumerate(deck):
        for compare in deck[index+1:]:
            if value == compare:
                points += 1
    return points


def rule2(deck, target):
    '''recursion. a point for all combinations of cards summing 15'''
    total = 0
    for index,value in enumerate(deck):
        if value == target:
            total += 1
        elif value < target and len(deck) > 1:
            total += rule2(deck[index+1:], target-value)
    return total


if debug:
    card1, card2, card3, card4, card5 = 3,3,3,2,10
else: card1, card2, card3, card4, card5  = input('enter 5 numbers 1-10 spearated by spaces: ').split(' ')

#create a list of the cards
cards = [int(card1), int(card2), int(card3), int(card4), int(card5)]

print('cards entered: ',cards)

pairs = rule1(cards)
print(f'found {pairs} pairs')

fifteens = rule2(cards, 15)
print(f'found {fifteens} fifteens')

print('Total = ',pairs + fifteens)