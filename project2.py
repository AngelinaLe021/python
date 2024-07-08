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
    def adjustForAce(self):
        for card in self.cards:
            if self.value > 21 and card.rank == 'Ace': 
                self.value -= 11
                self.value += 1

        # return self.value




testDeck = Deck()
testDeck.shuffle() 
testPlayer = Hand()
testPlayer.addCard(testDeck.deal())
testPlayer.addCard(testDeck.deal())
for card in testPlayer.cards:
    print(card)
# print(testPlayer.adjustForAce())
print(testPlayer.value)