import random

# Klass kaardi jaoks
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit

# Klass kaardipaki jaoks
class Deck:
    def __init__(self):
        self.deck = []
        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

# Klass mängija jaoks
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

# Kaartide väärtused
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}

# Klass mängija jaoks
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def hit(self, deck):
        self.hand.add_card(deck.deal())

    def stay(self):
        pass

# Klass diileri jaoks
class Dealer:
    def __init__(self):
        self.hand = Hand()

    def hit(self, deck):
        self.hand.add_card(deck.deal())

    def stay(self):
        pass

# Mängu funktsioon
def play_game():
    deck = Deck()
    deck.shuffle()
    player = Player("Player1")
    dealer = Dealer()
    player.hit(deck)
    player.hit(deck)
    dealer.hit(deck)
    dealer.hit(deck)
    print("Player's hand: ", *player.hand.cards, sep='\n')
    print("Dealer's hand: ", dealer.hand.cards[0], "and unknown card")
    while player.hand.value < 21:
        choice = input("Do you want to hit or stay? ")
        if choice == 'hit':