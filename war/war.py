import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:
    '''Represents a single card
    
    Attributes
    ----------
    suit : str
        the suit of a card
    rank : str
        the rank of a card
    value : int
        the value of a card'''
        
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit
    
class Deck:
    '''Represents a deck of 52 cards

    ...
    
    Attributes
    ----------
    all_cards : list
        stores the Cards of this deck
        
    Methods
    -------
    shuffle()
        Shuffles the deck of cards without returning anything
    deal_one()
        Pops and returns a card from the deck'''
    
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        '''Shuffles the cards stored in instance variable self.all_cards'''
        random.shuffle(self.all_cards)

    def deal_one(self):
        '''Returns the last card in self.all_cards'''
        return self.all_cards.pop()
    
    def __len__(self):
        return len(self.all_cards)
    
class Player:
    '''Represents a player
    
    ...
    
    Attributes
    ----------
    all_cards : list
        contains all the cards the Player is holding
    name : str
        name of the player
        
    Methods
    -------
    remove_one()
        Removes and returns the topmost Card
    add_cards(new_cards)
        Adds either a list of cards or a single Card to all_cards'''
    
    def __init__(self, name):
        self.name = name
        # A new player starts off with no cards
        self.all_cards = []

    def remove_one(self):
        '''Removes and returns the topmost Card'''
        return self.all_cards.pop(0)
    
    def add_cards(self, new_cards):
        '''Adds cards to the players hand

        Checks to see if multiple cards are being added as a list, or a single Card
        
        Parameters
        ----------
        new_cards : list or Card
            A card or cards that are being added to the players hand'''
        
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'
    
class War:

    def __init__(self, player_one_name, player_two_name):    
        #Two players per game
        self.player_one = Player(player_one_name)
        self.player_two = Player(player_two_name)

        #Rounds begin at 0 for every new game of War
        self.round = 0

        #Deal starting cards to players
        self.deal_starting_deck()

    def deal_starting_deck(self):
        '''Deals starting decks to player one and player two.
        
        Creates a new_deck and shuffles it. Then a loop alternates dealing
        individual cards to players.'''

        new_deck = Deck()
        new_deck.shuffle

        index = 0
        
        while(index < len(new_deck)):
            if index % 2 == 0:
                self.player_one.add_cards(new_deck.deal_one)
            else:
                self.player_two.add_cards(new_deck.deal_one)
            
            index += 1

    def is_out_of_cards(self, player):
        '''Checks to see if the player's deck is empty
        
        Parameters
        ----------
        player : Player
            an instance of Player
            
        Returns
        -------
        boolean
            True if the player is out of cards(lost), False otherwise'''
        
        return len(player.all_cards) == 0

new_game = War('Arsen', 'Lilit')
print(new_game.player_one)
print(new_game.player_two)
print(new_game.player_one.remove_one())