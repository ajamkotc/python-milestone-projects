import random
import unittest
import blackjack
import exceptions

class TestBlackjack(unittest.TestCase):
    '''Test suite for Blackjack card game

    Attributes
    ----------
    name : str
        placeholder name

    Tests
    -------
    test_deck_length
        Tests the length of the deck
    test_deck_duplicates
        Tests if the deck has any duplicate cards.
    test_shuffle
        Tests if the deck is sufficiently shuffled.
    test_deal_card
        Tests method deal_one in class Deck.
    test_deal_card_duplicate
        Tests if a Card is truly removed when deal_one() is called.
    test_add_money
        Tests if money is correctly added to the 'money' attribute.
    test_add_card
        Tests if a Player's add_cards correctly adds individual cards.
    test_place_bet
        Tests if Player's place_bet() works correctly.
    test_bet_exception
        Tests if Player's place_bet() correctly raises an Insufficient Funds Exception.
    test_total_points
        Tests if card values are correctly added.
    test_clear
        Tests if player's cards are completely cleared.
    test_out_money
        Tests method out_of_money when player's money is depleted.
    test_starting_player_deal
        Tests if player is dealt two cards at the beginning of a round.
    test_starting_dealer_deal
        Tests if dealer is dealt two cards at the beginning of a round.
    test_has_bust
        Tests if class method has_bust works properly.'''

    name = "Player"
    deck_length = 52

    # Tests for Deck class

    def test_deck_length(self):
        '''Tests the length of the deck.'''

        new_deck = blackjack.Deck()
        self.assertEqual(len(new_deck.all_cards), self.deck_length,
                         f"Deck has {len(new_deck.all_cards)}")

    def test_deck_duplicates(self):
        '''Tests if the deck has any duplicate cards.'''

        new_deck = blackjack.Deck()
        duplicate = False

        for index, card in enumerate(new_deck.all_cards):
            if card in new_deck.all_cards[index + 1:]:
                duplicate = True
                break

        self.assertFalse(duplicate, "Duplicate found.")

    def test_shuffle(self):
        '''Tests if the deck is sufficiently shuffled.

        Sufficiently shuffled if more or equally more cards are moved than cards
        left in the same position.'''

        new_deck = blackjack.Deck()
        other_deck = blackjack.Deck()
        new_deck.shuffle()

        same_location = 0
        different_location = 0

        for index, card in enumerate(new_deck.all_cards):
            if card == other_deck.all_cards[index]:
                same_location += 1
            else:
                different_location += 1

        self.assertGreaterEqual(different_location, same_location, "Deck has not been shuffled.")

    def test_deal_card(self):
        '''Tests method deal_one in class Deck.

        Picks a random number between 1 and the length of the Deck. That number of cards
        are dealt and then the remaining quantity of cards are compared to 52 - the random
        number.'''

        new_deck = blackjack.Deck()

        random_rep = random.randint(1, len(new_deck.all_cards))
        index = 0

        while index < random_rep:
            new_deck.deal_one()
            index += 1

        self.assertEqual(len(new_deck.all_cards), self.deck_length - random_rep)

    def test_deal_card_duplicate(self):
        '''Tests if a Card is truly removed when deal_one() is called.

        A random quantity of cards are dealt. Each time a card is dealt, the
        card is searched for in the list of cards in new_deck.'''

        new_deck = blackjack.Deck()

        random_rep = random.randint(1, len(new_deck.all_cards))
        index = 0
        duplicate = False

        while index < random_rep:
            dealt_card = new_deck.deal_one()

            if dealt_card in new_deck.all_cards:
                duplicate = True
                break

            index += 1

        self.assertFalse(duplicate)

    # Tests for Player class

    def test_add_money(self):
        '''Tests if money is correctly added to the 'money' attribute.'''

        new_player = blackjack.Player(self.name, 0)
        money = random.randint(0, 100)

        new_player.add_money(money)

        self.assertEqual(new_player.money, money, "Money not correctly added to player")

    def test_add_card(self):
        '''Tests if a Player's add_cards correctly adds individual cards.'''

        new_player = blackjack.Player(self.name)
        new_deck = blackjack.Deck()

        quantity = random.randint(1, len(new_deck))
        index = 0

        while index < quantity:
            new_player.add_card(new_deck.deal_one())

            index += 1

        self.assertEqual(quantity,len(new_player.cards),
                         f"{quantity} cards were dealt to player but they have {len(new_player.cards)} cards.")

    def test_place_bet(self):
        '''Tests if Player's place_bet() works correctly.'''

        starting_money = random.randint(1, 1000)
        new_player = blackjack.Player(self.name, starting_money)

        bet_amount = random.randint(1, starting_money)
        new_player.place_bet(bet_amount)

        self.assertEqual(new_player.money, starting_money - bet_amount,
                         "Incorrect amount subtracted from player's available money.")

    def test_bet_exception(self):
        '''Tests if Player's place_bet() correctly raises an Insufficient Funds Exception.
        when the bet amount is greater than the player's available money.'''

        starting_money = random.randint(1, 1000)
        new_player = blackjack.Player(self.name, starting_money)

        with self.assertRaises(exceptions.InsufficientFundsException):
            new_player.place_bet(starting_money + 1)

    def test_total_points(self):
        '''Tests if card values are correctly added.

        Ensures that ace values are switched to 1 if they would cause a
        bust if calculated a an 11.'''

        new_player = blackjack.Player(self.name)

        card_one = blackjack.Card("Ace", "Spades")
        card_two = blackjack.Card("Five", "Clubs")
        card_three = blackjack.Card("King", "Hearts")

        new_player.add_card(card_one)
        new_player.add_card(card_two)
        self.assertEqual(new_player.total_points(), 16, "Pre-assigned values not correctly added")

        new_player.add_card(card_one)
        self.assertEqual(new_player.total_points(), 17, "Ace value not correctly changed")

        new_player.add_card(card_three)
        self.assertEqual(new_player.total_points(), 17, "Face card value incorrectly added.")

        new_player.add_card(card_three)
        self.assertEqual(new_player.total_points(), 27, "Face card value incorrectly added.")

    def test_clear(self):
        '''Tests if player's cards are completely cleared.'''

        new_deck = blackjack.Deck()
        new_player = blackjack.Player(self.name)

        card_amount = random.randint(1, self.deck_length)
        index = 0

        while index in range(0, card_amount):
            new_player.add_card(new_deck.deal_one())
            index += 1

        new_player.clear_cards()

        self.assertEqual(len(new_player.cards), 0, "Player deck not completely cleared.")

    def test_out_money(self):
        '''Tests method out_of_money when player's money is depleted.'''

        money = random.randint(1, 100)
        new_player = blackjack.Player(self.name, money)

        new_player.place_bet(money)

        self.assertTrue(new_player.out_of_money(), "Player should be out of money.")

    # Tests for Blackjack class

    def test_starting_player_deal(self):
        '''Tests if player is dealt two cards at the beginning of a round.'''

        new_game = blackjack.Blackjack(self.name)
        new_game.deal_starting_round()

        self.assertEqual(len(new_game.player.cards), 2, "Player not dealt 2 starting cards.")

    def test_starting_dealer_deal(self):
        '''Tests if dealer is dealt two cards at the beginning of a round.'''

        new_game = blackjack.Blackjack(self.name)
        new_game.deal_starting_round()

        self.assertEqual(len(new_game.dealer.cards), 2, "Dealer not dealt two starting cards.")

    def test_has_bust(self):
        '''Tests if class method has_bust works properly.'''

        new_player = blackjack.Player(self.name)
        new_player.add_card(blackjack.Card("King", "Spades"))
        new_player.add_card(blackjack.Card("King", "Hearts"))
        self.assertFalse(blackjack.Blackjack.has_bust(new_player), "Player has not bust.")

        new_player.add_card(blackjack.Card("Two", "Diamonds"))
        self.assertTrue(blackjack.Blackjack.has_bust(new_player), "Player should have bust.")

if __name__ == '__main__':
    unittest.main()
