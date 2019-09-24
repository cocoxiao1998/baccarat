from scipy.stats import hypergeom
import deck

#proability that the card will be drawn
def hyper_geometric_help(total_cards, cards):
    return hypergeom.pmf(1, total_cards, cards, 1, loc=0)

def total_cards(deck):
    #player does not know one of the dealer's card
    return deck.getsize() + 1

#0 for helpful cards, 1 for cards that will do nothing
def cards(player, dealer, flag):
    if flag == 0:
        #the value that will help and the numbers below it too
        value = 9 - player.getScore()

        #total number of cards that will help
        total = value * 4

        #checking player's 2 cards and the dealer's face up card
        if player.cardsHeld[0].value <= value:
            total -= 1
        if player.cardsHeld[1].value <= value:
            total -= 1
        if dealer.cardsHeld[0].value <= value:
            total -= 1

    if flag == 1:
        total = 16

        #checking player's 2 cards and the dealer's face up card
        if player.cardsHeld[0].value <= 0:
            total -= 1
        if player.cardsHeld[1].value <= 0:
            total -= 1
        if dealer.cardsHeld[0].value <= 0:
            total -= 1

    return total


