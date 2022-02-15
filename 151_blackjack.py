from enum import Enum
import random

class Suit(str, Enum): 
    Club="♣" 
    Diamond="♦" 
    Heart="♥" 
    Spade="♠" 

class Rank(Enum):
    Ace="A"
    two=2
    three=3
    four=4
    five=5
    six=6
    seven=7
    eight=8
    nine=9
    ten=10
    Jack=10
    Queen=10
    King=10

def Rank1():
    return Rank
def Suit1():
    return Suit

class BlackJackCard:
    rank= Rank1()
    suit= Suit1()

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        rep = str(self.rank.value) + " " + str(self.suit.value)
        return rep

class Hand: 
    def __init__(
        self, 
            dealer_card: BlackJackCard, 
            *cards: BlackJackCard 
        ) -> None: 
        self.dealer_card = dealer_card
        self._cards = list(cards)

class Hand_Lazy(Hand): 
    @property
    def total(self) -> int:

        result=0
        has_ace=False
        for c in self._cards:
            if "Ace" == c.rank.name:
                has_ace=True
                result += 11
            else:
                result +=c.rank.value

        if has_ace and result >= 21:
            return result-10
        else:
            return result

    @property 
    def card(self):
        return self._cards  

    @card.setter
    def card(self, aCard: BlackJackCard) -> None:

        self._cards.append(aCard)

    @card.deleter 
    def card(self) -> None: 
        self._cards.pop(-1)

class Deck():
    def create_deck(self):
        new_deck = []
        card_ranks = Rank1()
        card_suits = Suit1()

        for rank in card_ranks:
            for suit in card_suits:
                new_deck.append(BlackJackCard(rank, suit))
        random.shuffle(new_deck)
        return new_deck

d = Deck()
deck=d.create_deck()
print("Shuffeled deck:")
for i in deck:
    print(i)

#fist card is the dealer one
h = Hand_Lazy(deck.pop(), deck.pop(), deck.pop())
print("Total:", h.total)