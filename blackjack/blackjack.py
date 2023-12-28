import random
from colorama import Fore
import exceptions

suits = {"Spades", "Clubs", "Hearts", "Diamonds"}
ranks = {"Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
         "Nine", "Ten", "Jack", "Queen", "King", "Ace"}
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8,
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

    def __init__(self, name, money=100):
        self.name = name
        self.money = money
        self.cards = []

    def place_bet(self, amount):
        '''Method to handle setting a bet.

        If the bet amount is greater than the player's available funds, an error
        is raised.

        Params
        ------
        amount : int
            the amount of a bet'''

        if amount <= self.money:
            self.money -= amount
        else:
            raise exceptions.InsufficientFundsException

    def clear_cards(self):
        '''Clears the player's cards in order to start a new round.'''

        self.cards.clear()

    def add_money(self, amount):
        '''Adds money to the player's bank.

        Params
        ------
        amount : int
            amount of money to be added'''

        self.money += amount

    def out_of_money(self):
        '''Checks if player is out of money.

        Returns
        -------
        bool
            True if out of money, False otherwise'''

        return self.money == 0

    def add_card(self, card):
        '''Adds cards to the player's hand.

        Params
        ------
        card : Card
            card to be added to the player's hand'''

        self.cards.append(card)
        self.cards.sort(key=lambda card: card.value)

    def total_points(self):
        '''Calculates the total points of the player's hand.

        If ace will cause player to bust, value is changed to 1.

        Returns
        -------
        total : int
            total value of the hand'''

        total = 0

        for card in self.cards:
            if card.rank == "Ace" and (total + card.value) > 21:
                card.value = 1
                total += card.value
            else:
                total += card.value

        return total

    def __str__(self):
        return_string = f"{self.name}'s hand consists of:\n"

        for card in self.cards:
            return_string += str(card) + "\n"

        return return_string

class Blackjack:
    '''Class to handle aspects and logic of Blackjack.

    Attributes
    ----------
    player : Player
        represents the player
    dealer : Player
        represents the dealer
    cards : Deck
        deck being used for the game
    bet : int
        bet amount for each round

    Methods
    -------
    deal_starting_round()
        Deals starting hand of two cards first to the player then the dealer.
    dealer_round()
        Dealer deals themselves cards as long as they have less than 17 points.
    prompt_player()
        Prompts the player to hit or stand.
    prompt_player_bet()
        Prompts the player for a bet amount.
    prompt_player_round()
        Asks the user if they would like to continue playing.
    player_round()
        Player's round.
    game()
        Method to carry out logic of the game of Blackjack.

    Class Methods
    -------------
    has_bust(player)
        Checks to see if player's hand caused them to bust.'''

    def __init__(self, starting_amount, player_name="Player"):
        self.player = Player(player_name, starting_amount)
        self.dealer = Player("Dealer")

        self.cards = Deck()
        self.cards.shuffle()

        self.bet = 0

    def deal_starting_round(self):
        '''Deals starting hand of two cards first to the player then the dealer.'''

        self.player.add_card(self.cards.deal_one())
        self.player.add_card(self.cards.deal_one())

        self.dealer.add_card(self.cards.deal_one())
        self.dealer.add_card(self.cards.deal_one())

    def dealer_round(self):
        '''Dealer deals themselves cards as long as they have less than 17 points.'''
        print(Fore.BLUE + f"\nDealer flips over a {self.dealer.cards[1]}\n")

        while self.dealer.total_points() < 17:
            new_card = self.cards.deal_one()
            print(f"Dealer deals themselves a {new_card}")
            self.dealer.add_card(new_card)

    def prompt_player(self):
        '''Prompts the player to hit or stand.

        Returns
        -------
        player_input: str
            player's choice to hit or stand'''

        menu_options = ["hit", "stand"]

        while True:
            try:
                player_input = input(Fore.WHITE + "Would you like to 'hit' or 'stand': ")

                if player_input.lower() not in menu_options:
                    raise exceptions.InputException
            except exceptions.InputException:
                print(Fore.RED + "Invalid input. Please select from the provided options\n")
                continue
            else:
                break

        return player_input

    def prompt_player_bet(self):
        '''Prompts the player for a bet amount.

        Raises a ValueError if a non-integer is inputted.
        Raises an InsufficientFundsException if a bet amount greater than the
        available funds is inputted.

        Returns
        -------
        player_input : int
            stores the player's selected bet amount'''

        print(Fore.WHITE + f"{self.player.name} has {self.player.money} dollars available.")
        while True:
            try:
                player_input = input(Fore.WHITE + "Please enter bet amount: ")

                if int(player_input) > self.player.money:
                    raise exceptions.InsufficientFundsException
            except ValueError:
                print(Fore.RED + "Please input an integer value")

                continue
            except exceptions.InsufficientFundsException:
                print(Fore.RED + "You entered an amount greater than your available funds.")
                print(f"Available funds: {self.player.money}")

                continue
            else:
                break

        return int(player_input)

    def prompt_player_round(self):
        '''Asks the user if they would like to continue playing.

        Returns
        -------
        player_choice : str
            returns 'y' to continue and 'n' to quit'''

        choices = ('y', 'n')
        player_choice = ''

        while True:
            try:
                player_choice = input(Fore.WHITE + "Would you like to play another round? (y/n): ")

                if player_choice.lower() not in choices:
                    raise exceptions.InputException
            except exceptions.InputException:
                print(Fore.RED + "Invalid choice. Please enter 'y' for yes and 'n' for no")
                continue
            else:
                break

        return player_choice

    def player_round(self):
        '''Player's round.

        Player sets their bet, gets dealt their starting round, and then is asked
        to hit or stand until they choose to stand or bust.'''

        print(Fore.GREEN + f"{self.player.name}, you're up!\n")
        self.bet = self.prompt_player_bet()
        self.player.place_bet(self.bet)

        self.deal_starting_round()
        print(Fore.GREEN +
              f"\n{self.player.name}'s cards: {self.player.cards[0]} and a {self.player.cards[1]}")
        print(Fore.BLUE + f"Dealer's faceup card is a: {self.dealer.cards[0]}\n")

        while not Blackjack.has_bust(self.player) and self.prompt_player() == 'hit':
            new_card = self.cards.deal_one()
            self.player.add_card(new_card)
            print(Fore.GREEN + f"{self.player.name} was dealt a {new_card}\n")

    def game(self):
        '''Method to carry out logic of the game of Blackjack.'''

        continue_game = 'y'

        while continue_game == 'y':
            # Clear hands when starting a new round
            self.player.clear_cards()
            self.dealer.clear_cards()

            # Player first plays their round
            self.player_round()
            player_points = self.player.total_points()

            if self.has_bust(self.player):
                # If the player busts, they automatically lose.
                print(Fore.RED + f"{self.player.name} bust! Dealer wins this round")
            else:
                # Dealer hits until they have at least 17
                self.dealer_round()
                dealer_points = self.dealer.total_points()

                if self.has_bust(self.dealer):
                    # If the dealer busts, the player wins
                    print(Fore.GREEN + f"Dealer bust! {self.player.name} wins.")

                    self.player.add_money(self.bet * 2)
                elif dealer_points < player_points:
                    # If neither have busted and the player scores more points
                    print(Fore.GREEN +
                          f"Dealer scored {dealer_points} points, {self.player.name} scored {player_points} points.")
                    print(f"{self.player.name} wins!")

                    self.player.add_money(self.bet * 2)
                elif player_points < dealer_points:
                    # If neither have busted but the dealer scores more points
                    print(Fore.RED + f"Dealer scored more points. {self.player.name} loses.")
                else:
                    # In case of a tie
                    print(Fore.BLUE + "Tie!")

                    self.player.add_money(self.bet)

            if self.player.out_of_money():
                print(Fore.RED + "You are all out of money. Try again next time")
                break

            continue_game = self.prompt_player_round()

    @classmethod
    def has_bust(cls, player):
        '''Checks to see if player's hand caused them to bust.

        Params
        ------
        player : Player
            player whose hand will be tested

        Returns
        -------
        bool
            True if has bust, False otherwise'''

        score = player.total_points()

        return score > 21

if __name__ == '__main__':
    print("Welcome to Blackjack!")
    input_name = ''
    input_money = 0

    while True:
        try:
            input_name = input("Please enter your name: ")

            if len(input_name) < 1:
                raise exceptions.InvalidNameException
        except exceptions.InvalidNameException:
            print("Incorrect name. Please enter at least one character.")
            continue
        else:
            break

    while True:
        try:
            input_money = int(input("Please enter your starting money amount: "))
        except ValueError:
            print("Please enter an integer for your starting money amount.")
            continue
        else:
            break

    print()
    new_game = Blackjack(input_money, input_name)
    new_game.game()
