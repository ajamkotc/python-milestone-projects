import random

suits = {"Spades", "Clubs", "Hearts", "Diamonds"}
ranks = {"Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
         "Nine", "Ten", "Jack", "Queen", "King", "Ace"}
values = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8,
          "Nine": 9, "Ten": 10, "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}

class Card:
    '''Class Card represents a single Card.

    Attributes
    ----------
    rank : str
        the rank of a card represented by a string
    suit : str
        the suit of a card
    value : int
        the value of a card based on its rank'''

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self):
        '''Returns a string representation of a Card in the format Rank of Suits.

        Returns
        -------
        String
            self.rank of self.suit'''

        return f"{self.rank} of {self.suit}"

    def __gt__(self, other_card):
        '''Overrides '>' operator when comparing two Card instances.

        Params
        ------
        other_card : Card
            Card with which instance of current card is being compared

        Returns
        -------
        Boolean
            True if Card on the left of '>' operator is greater than Card on the right'''
        return self.value > other_card.value

    def __lt__(self, other_card):
        '''Overrides '<' operator when comparing two Card instances.

        Params
        ------
        other_card : Card
            Card with which instance of current card is being compared

        Returns
        -------
        Boolean
            True if Card on the left of '<' operator is greater than Card on the right'''

        return self.value < other_card.value

    def __eq__(self, other_card):
        return (self.rank == other_card.rank) and (self.suit == other_card.suit)

class Deck:
    '''Class Deck represents an entire deck of Cards.

    Attributes
    ----------
    all_cards : list
        a list of Cards

    Methods
    -------
    shuffle()
        Shuffles the list of cards using random.shuffle()
    deal_one()
        Pops and returns the last card in the Deck'''

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(rank, suit))

    def shuffle(self):
        '''Shuffles the deck.'''

        random.shuffle(self.all_cards)

    def deal_one(self):
        '''Deals the bottom Card from the Deck.

        Returns
        -------
        Card
            the last Card in all_cards'''

        return self.all_cards.pop()

    def __str__(self):
        '''Provides a string representation of Deck.

        Converts Deck into a list of each Card.

        Returns
        -------
        String
            list including every single card'''

        str_representation = ''

        for card in self.all_cards:
            str_representation += f"{str(card)}\n"

        return str_representation

    def __contains__(self, card):
        return card in self.all_cards

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def add_cards(self, cards):
        if type(cards) == type([]):
            self.cards.extend(cards)
        else:
            self.cards.append(cards)

if __name__ == '__main__':
    new_deck = Deck()
    print(new_deck)
    new_deck.shuffle()
    print(new_deck)