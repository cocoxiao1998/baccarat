import deck
import hyper_geometric as hg

def main():
    flag = 'y'
    while flag == 'y':
        #checking for natural 9
        #0 for none
        #1 for dealer
        #2 for player
        #3 for tie
        default_win = 0  

        #creating deck
        card_deck = deck.Deck()

        #dealer/Pratt receives 2 cards    
        dealer = deck.Dealer()
        dealer.receive(card_deck)
        card_deck.shuffle()
        dealer.receive(card_deck)
        card_deck.shuffle()

		#displaying dealer's face up card
        print("\nDealer's face up card: ")
        print(dealer.cardsHeld[0].rank, " of", dealer.cardsHeld[0].suit)
        input("\nPress Enter to continue...")

		#displaying dealer's cards 
        print("\nDealer's hand: ")
        dealer.getHand()

        #player/computer receives 2 cards
        player = deck.Player()
        player.receive(card_deck)
        card_deck.shuffle()
        player.receive(card_deck)
        card_deck.shuffle()
        
        #displaying player's cards
        print("\nPlayer's hand: ")
        player.getHand()

		#if dealer has 9 as their face-up card, check if total is equal to 9
        if dealer.cardsHeld[0].value == 9:
            if dealer.getScore() == 9:
                if dealer.getScore() == player.getScore():
                    default_win = 3
                else: 
                    default_win = 1

        if player.getScore() == 9:
            if player.cardsHeld[0].value == 9 or player.cardsHeld[1].value == 9:
                if dealer.getScore() == player.getScore():
                    default_win = 3
                else:
                    default_win = 2

        if default_win == 0:
            #player logic
            #finding probability that new card for player will help
            good_p = hg.hyper_geometric_help(hg.total_cards(card_deck), hg.cards(player, dealer, 0))
            neutral_p= hg.hyper_geometric_help(hg.total_cards(card_deck), hg.cards(player, dealer, 1))
            print("\nProbability:")
            print("Helpful cards: %.2f" % good_p)
            print("Neutral cards: %.2f" % neutral_p)

            if player.getScore() >= 7:
                print("\nPlayer does not take the hit")
            else:
                if (good_p + neutral_p) > .57:
                    player.receive(card_deck)
                    print("\nPlayer's new hand: ")
                    player.getHand()

			#dealer logic
            if dealer.getScore() <= 4:
                dealer.receive(card_deck)
                print("\nDealer's new hand: ")
                dealer.getHand()
            else:
                print("\nDealer does not take the hit")
            
            #checking who wins
            if dealer.getScore() > player.getScore():
                deck.Player.lose()
            elif dealer.getScore() < player.getScore():
                deck.Player.win()
            else: 
                deck.Player.tie()
        elif default_win == 1:
            deck.Player.lose()
        elif default_win == 2:
            deck.Player.win()
        else:
            deck.Player.tie()

        #calling stats
        deck.Player.stats()

        #checking if dealer wants to play another game
        flag = input("\nDo you want to play another game. Enter 'y' for yes, enter anything else to close: ")
        print("\n")

if __name__ == "__main__":
    main()
        