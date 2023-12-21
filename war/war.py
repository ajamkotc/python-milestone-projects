import random
import exceptions

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
         'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7,
          'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

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
        return self.rank + ' of ' + self.suit + f" Value: {self.value}"

    def __eq__(self, other_card):
        return ((self.suit == other_card.suit) and (self.rank == other_card.rank))

    def __gt__(self, other_card):
        return self.value > other_card.value

    def __lt__(self, other_card):
        return self.value < other_card.value

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
        return f'{self.name} has {len(self.all_cards)} cards.'

class War:
    '''Contains the logic and elements of a game of War

    Attributes
    ----------
    player_one : Player
        stores the name of player one as well as their cards
    player_two : Player
        stores the name of player two as well as their cards

    Methods
    -------
    deal_starting_deck()
        Deals 26 cards to each Player from a new Deck
    is_out_of_cards(player)
        Checks if a player is out of cards
    play_round()
        Plays one round of War
    play_game()
        Plays an entire game of War consisting of multiple rounds'''

    def __init__(self, player_one_name, player_two_name):
        # Two players per game
        self.player_one = Player(player_one_name)
        self.player_two = Player(player_two_name)

        # Deal starting cards to players
        self.deal_starting_deck()

    def deal_starting_deck(self):
        '''Deals starting decks to player one and player two.

        Creates a new_deck and shuffles it. Then a loop alternates dealing
        individual cards to players.'''

        new_deck = Deck()
        new_deck.shuffle()

        index = 0

        while index < 52:
            if index % 2 == 0:
                self.player_one.add_cards(new_deck.deal_one())
            else:
                self.player_two.add_cards(new_deck.deal_one())

            index += 1

    @classmethod
    def is_out_of_cards(cls, player):
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

    def play_round(self):
        '''Plays a round of War.'''

        # Flip over one card
        player_one_cards = [self.player_one.remove_one()]
        player_two_cards = [self.player_two.remove_one()]

        print(f"{self.player_one.name} played a {player_one_cards[0]}")
        print(f"{self.player_two.name} played a {player_two_cards[0]}\n")

        if player_one_cards[0] > player_two_cards[0]:
            print(f"{self.player_one.name} Wins this Round")
            # Player one takes all cards if their card is larger in value
            self.player_one.add_cards(player_two_cards + player_one_cards)
        elif player_two_cards[0] > player_one_cards[0]:
            print(f"{self.player_two.name} Wins this Round")
            # Player two takes all cards if their card is larger in value
            self.player_two.add_cards(player_one_cards + player_two_cards)
        else:
            # Both cards are equal so there is War
            print("War!")
            while True:
                try:
                    # Two more cards are removed from player 1's deck
                    player_one_cards.append(self.player_one.remove_one())
                    player_one_cards.append(self.player_one.remove_one())
                except IndexError:
                    print(f"{self.player_one.name} does not have enough cards for War.")
                    break

                try:
                    player_two_cards.append(self.player_two.remove_one())
                    player_two_cards.append(self.player_two.remove_one())
                except IndexError:
                    print(f"{self.player_two.name} does not have enough cards for War.")
                    break

                player_one_war_card = player_one_cards[len(player_one_cards) - 1]
                player_two_war_card = player_two_cards[len(player_two_cards) - 1]

                print(f"{self.player_one.name}'s Card: {player_one_war_card}")
                print(f"{self.player_two.name}'s Card: {player_two_war_card}")

                # Compare the last card flipped over
                if player_one_war_card > player_two_war_card:
                    print(f"{self.player_one.name} Wins This War")
                    self.player_one.add_cards(player_two_cards + player_one_cards)
                    break
                elif player_two_war_card > player_one_war_card:
                    print(f"{self.player_two.name} Wins This War")
                    self.player_two.add_cards(player_one_cards + player_two_cards)
                    break
                else:
                    print("Tie!")

    def play_game(self):
        '''Plays multiple rounds of War until a player runs out of cards'''

        while not War.is_out_of_cards(self.player_one) and not War.is_out_of_cards(self.player_two):
            input("\nPress any key to play a round...\n")

            print(self.player_one)
            print(f"{self.player_two}\n")

            self.play_round()

            if War.is_out_of_cards(self.player_one):
                print(f"{self.player_two.name} won!")
            elif War.is_out_of_cards(self.player_two):
                print(f"{self.player_one.name} won!")
            else:
                continue

if __name__ == "__main__":
    print("Welcome to the Game of War!")

    while True:
        try:
            player_one_input = input("Please enter Player One's Name: ")
            if len(player_one_input) < 1:
                raise exceptions.InvalidNameException
        except exceptions.InvalidNameException:
            print("Please enter at least one character for the name")
            continue
        else:
            break

    while True:
        try:
            player_two_input = input("Please enter Player Two's Name: ")
            if len(player_two_input) < 1:
                raise exceptions.InvalidNameException
        except exceptions.InvalidNameException:
            print("Please enter at least one character for the name")
            continue
        else:
            break

    new_game = War(player_one_input, player_two_input)
    new_game.play_game()
