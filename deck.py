import random

class Card:
    #Card class has instance attributes: suit, rank and value
    #value ranges from 0-9 since the game is baccarat

    def __init__(self, suit, rank):
        #suit converter
        if suit == 1:
            self.suit = "Spades"
        if suit == 2:
            self.suit = "Clubs"
        if suit == 3:
            self.suit = "Diamonds"
        if suit == 4:
            self.suit = "Hearts"
        #rank and value converter
        if rank == 10:
            self.rank = rank
        if rank == 11:
            self.rank = "J"
        if rank == 12:
            self.rank = "Q"
        if rank == 13:
            self.rank = "K"
        if rank >= 10:
            self.value = 0
        else:
            self.value = rank
            self.rank = rank

        if rank == 1:
            self.rank = "A"

    def getcard(self):
        return self

class Deck:
    #initializes the deck and the cards for the deck and stores them in the list
    def __init__(self):
        self.DeckArr = []
        for x in range(1, 5):
            for y in range(1, 14):
                self.DeckArr.append(Card(x, y)) 
        #calling to shuffle after initialization of deck
        self.shuffle()

    #randomly shuffles cards in deck
    def shuffle(self):
        #trying to make random library more random with a seed
        random.seed(None, 2) 
        for x in range(0,200):
            j = random.randint(0, self.getsize() - 1)
            k = random.randint(0, self.getsize() - 1)
            #swapping cards in deck places
            temp = self.DeckArr[k]
            self.DeckArr[k] = self.DeckArr[j]
            self.DeckArr[j] = temp

    #returns a card from the deck class to give to the dealer or the player's receive function
    def getcard(self):
        returnvalue = self.DeckArr.pop() #store the popped value to return to the player or dealer
        return returnvalue

    #returns the current size of the deck
    def getsize(self):
        return len(self.DeckArr)

class Player:
    wins = 0
    losses = 0
    ties = 0

    def __init__(self):
        self.cardsHeld = []
        self.currentScore = 0

    #to get a card
    def receive(self, deck): #receives pulled card from the deck's getcard function
        self.cardsHeld.append(deck.getcard())

    def getScore(self):
        self.currentScore = 0
        for card in self.cardsHeld:
            self.currentScore += card.value
        if self.currentScore > 9:
                self.currentScore = self.currentScore%10
        return self.currentScore

    def getHand(self): #plays
        for x in self.cardsHeld:
            print(x.rank, " of ", x.suit)

    #regarding wins losses and conditions, use only for player
    @staticmethod
    def win():
        print("\nThe player wins!")
        Player.wins += 1
    @staticmethod
    def lose():
        print("\nThe dealer wins!")
        Player.losses += 1
    @staticmethod
    def tie():
        print("\nIt's a tie!")
        Player.ties += 1

    #report wins and losses
    @staticmethod
    def stats():
        print("\nPlayer's stats:")
        print("---------------")
        print("Wins:", Player.wins, "\nLosses:", Player.losses, "\nDraws:", Player.ties)

class Dealer:
    def __init__(self):
        self.cardsHeld = []
        self.currentScore = 0

    def receive(self, deck):
        self.cardsHeld.append(deck.getcard())

    def getHand(self):
        for x in self.cardsHeld:
            print(x.rank, " of ", x.suit)

    def getScore(self):
        self.currentScore = 0
        for x in self.cardsHeld:
            self.currentScore += x.value
        if self.currentScore > 9:
                self.currentScore = self.currentScore%10
        return self.currentScore
