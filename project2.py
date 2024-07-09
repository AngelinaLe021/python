# BLACKJACK

import random 

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True

class Card: 
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return self.rank + ' of ' + self.suit
    
class Deck:
    def __init__(self):
        self.allCards = []
        for suit in suits: 
            for rank in ranks:
                self.allCards.append(Card(suit, rank))
                # print(self.allCards)
    def __str__(self):
        deckComp = ''
        for card in self.allCards:
            deckComp += '\n' + card.__str__() 
        return 'The deck has: ' + deckComp
        
    def shuffle(self):
        random.shuffle(self.allCards)
    def deal(self): 
        return self.allCards.pop()
    
class Hand:
    def __init__(self):
        self.cards = [] # Start with an empty list as we did in the Deck class
        self.value = 0 # Start with 0 value
        self.aces = 0 # Add an attribute to keep track of aces

    def addCard(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1 # Add to self.aces
    def adjustForAce(self):
        while self.value > 21 and self.aces: 
            self.value -= 10
            self.aces -= 1

class Chips:
    def __init__(self, total = 100):
        self.total = total # This can be set to a default value or supplied by a user input
        self.bet = 0

    def winBet(self):
        self.total += self.bet
    def loseBet(self):
        self.total -= self.bet

def takeBet(chips):
    chips.bet = input("How many chips you would like to bet? ")
    while (chips.bet.isdigit() == False and type(chips.bet) != int) or (int(chips.bet) < 1):
        print("Wrong Input! Whole number that's greater than 0 ONLY!")
        chips.bet = input("Please place your bet again: ")
    while int(chips.bet) > int(chips.total): 
        print("You don't have enough chip to play.")
        print("Your total chips are", chips.total)
        chips.bet = input(f"Please place your bet that's less than or equal to {chips.total} chips: ")
    chips.bet = int(chips.bet)

def hit(deck, hand):
    hand.addCard(deck.deal())
    hand.adjustForAce()

def hitOrStand(deck, hand, chips):
    global playing

    while playing and hand.value <= 21: 
        choice = input("\nWould you like to Hit or Stand? Enter H or S: ")
        if choice.lower() == 'h':
            hit(deck, hand)
            print("\nPlayer's Hand: ", *hand.cards, sep = '\n')
            print("Player's Hand =", hand.value)
            if hand.value > 21: 
                print("\nPlayer Bust!")
                chips.loseBet()
                playing = False
                break
        elif choice.lower() == 's':
            print("\nPlayer stands. Dealer is playing.")
            playing = False
        else: 
            print("Sorry, please try again!")

def showSome(player, dealer):
    print("\nDealer's Hand: ")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand: ", *player.cards, sep = '\n')
    print("Player's Hand =", player.value)

def showAll(player, dealer):
    print("\nDealer's Hand: ", *dealer.cards, sep = '\n')
    print("Dealer's Hand = ", dealer.value)
    print("\nPlayer's Hand: ", *player.cards, sep = '\n')
    print("Player's Hand = ", player.value)

def playerWins(player, dealer, chips):
    print("\nPlayer Wins!")
    chips.winBet()

def dealerBusts(player, dealer, chips):
    print("\nDealer Busts!")
    chips.winBet()

def dealerWins(player, dealer, chips):
    print("\nDealer Win!")
    chips.loseBet()

def push(player, dealer):
    print("\nDealer and Player tie. It's a push!")

def blackJack():
    global playing
    while True:
        # Opening Statement
        print(" Welcome to BLACKJACK! Get as close to 21 as you can without going over \n\
          Dealer hits until she reaches 17. Aces count as 1 or 11.")
    
        deck = Deck()
        deck.shuffle()

        playerHand = Hand()
        playerHand.addCard(deck.deal())
        playerHand.addCard(deck.deal())

        dealerHand = Hand()
        dealerHand.addCard(deck.deal())
        dealerHand.addCard(deck.deal())

        chips = input("How many chips do you have? ")
        while chips.isdigit() == False or int(chips) < 1: 
            print("Invalid!")
            chips = input("Please enter a whole number that's greater than 1 for your total chips amount: ")
        chips = int(chips)
        playerChips = Chips(chips)

        takeBet(playerChips)
        showSome(playerHand, dealerHand)

        while playing:
            hitOrStand(deck, playerHand, playerChips)

        
        # If player's hand hasn't busted, playu dealer hand until reach 17
        if playerHand.value <= 21:
            while dealerHand.value < 17:
                hit(deck, dealerHand)

            # Show all cards
            showAll(playerHand, dealerHand)

            if dealerHand.value > 21:
                dealerBusts(playerHand, dealerHand, playerChips)
            if dealerHand.value > playerHand.value and dealerHand.value <= 21: 
                dealerWins(playerHand, dealerHand, playerChips)
            if dealerHand.value < playerHand.value:
                playerWins(playerHand, dealerHand, playerChips)
            if dealerHand.value == playerHand.value: 
                push(playerHand, dealerHand)

        print("\nPlayer's winning total: ", playerChips.total)

        newGame = input('\nWould you like to play another game? Enter Y or N ')
        if newGame == 'y' or newGame == 'Y': 
            playing = True
        else: 
            print("\nThanks for playing!")
            return
        
blackJack()