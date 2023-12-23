import random

suits = {"Spades", "Clubs", "Hearts", "Diamonds"}
ranks = {"Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
         "Nine", "Ten", "Jack", "Queen", "King", "Ace"}
values = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8,
          "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}

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
        '''Overrides '>' operator and compares two cards by their values..

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
        '''Overrides '<' operator and compares two cards by their values.

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
        '''Overrides '==' operator when comparing two Card instances.

        Two cards are equal if their rank and suit are the same.'''

        return (self.rank == other_card.rank) and (self.suit == other_card.suit)

    def __add__(self, other_card):
        '''Overrides the '+' operator.

        Adds one cards value to the other's.'''

        return self.value + other_card.value

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

    def __len__(self):
        return len(self.all_cards)

class Player:
    '''Player class representing a Blackjack player.

    Attributes
    ----------
    name : str
        name of the player
    cards : list
        cards belonging to the player

    Methods
    -------
    add_cards(cards)
        Adds cards to players 'cards' attribute'''

    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.cards = []

    def add_cards(self, cards):
        '''Adds cards to the player's hand.

        Params
        ------
        cards : list or Card'''

        if type(cards) == type([]):
            self.cards.extend(cards)
        else:
            self.cards.append(cards)

    def total_points(self):
        total = 0

        for card in self.cards:
            total += card.value

        return total

    def has_ace(self):
        '''Checks to see if a player has an Ace.

        Returns
        -------
        bool
            True if has an ace, False otherwise'''

        for card in self.cards:
            if card.rank == "Ace":
                return True
        return False

    def __str__(self):
        return f"{self.name} has {len(self.cards)} cards."

class Blackjack:
    def __init__(self, player_name):
        self.player = Player(player_name)

        self.cards = Deck()
        self.cards.shuffle()

        self.current_bet = 0

    def add_bet(self, bet):
        self.current_bet += bet

    @classmethod
    def has_bust(cls, player):
        score = player.total_points()

        if score <= 21:
            # If the player has not bust
            return False
        elif score > 21 and player.has_ace():
            # If the player has bust but has an ace whose value can be changed
            pass
        else:
            # Player has bust
            return True

if __name__ == '__main__':
    pass