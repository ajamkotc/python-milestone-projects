import unittest
import war

class TestWar(unittest.TestCase):
    '''Test suite for card game War.

    Methods
    -------
    test_deck_length()
        Tests if 52 cards are generated when a new Deck is formed
    test_deck_unique()
        Tests if there are any duplicates in the Deck
    test_card_gt()
        Tests if the greater than operator correctly compares two cards
    test_card_lt()
        Tests if the less than operator corectly compares two cards
    test_player_one_hand_count()
        Tests if Player One is dealt 26 cards at the start of the game
    test_player_two_hand_count()
        Tests if Player Two is dealt 26 cards at the start of the game
    test_player_hand_duplicates()
        Tests if a card is duplicated in both players' starting hands
    test_out_of_cards()
        Tests if class method out_of_cards in War returns True for an empty hand
    test_out_of_cards_false()
        Tests if class method out_of_cards in War returns False for a player with at least
        one card'''

    def test_deck_length(self):
        '''Tests if 52 cards are generated when a new Deck is formed'''

        new_deck = war.Deck()
        self.assertEqual(len(new_deck), 52, "Deck does not contain 52 cards")

    def test_deck_unique(self):
        '''Tests if there are any duplicates in the Deck'''

        new_deck = war.Deck()
        duplicate = False

        index = 0

        while index < 52 and not duplicate:
            bottom_card = new_deck.deal_one()
            duplicate = bottom_card in new_deck.all_cards

            index += 1

        self.assertFalse(duplicate, f"Duplicate found: {bottom_card}")

    def test_card_gt(self):
        '''Tests if the greater than operator correctly compares two cards

        A new deck is first sorted by increasing Card value. Then cards of the same value
        are compared with all cards of greater value. If a card of lower value is
        considered greater than a card of greater value, greater_than is set to True.'''

        new_deck = war.Deck()
        new_deck.all_cards.sort(key=lambda card: card.value)

        greater_than = False
        value_set = 4

        while value_set < 52:
            for card in new_deck.all_cards[:value_set]:
                for greater_card in new_deck.all_cards[value_set:]:
                    if card > greater_card:
                        greater_than = True
                        break

                if greater_than:
                    break

            value_set += 4

        self.assertFalse(greater_than, f"{card} is not greater than {greater_card}")

    def test_card_lt(self):
        '''Tests if the less than operator corectly compares two cards

        First sorts a new deck by card value. Then it compares cards of a value
        with cards of greater values. If the '<' operator does not work correctly
        less_than will equal to false and the loops will be broken out of.'''

        new_deck = war.Deck()
        new_deck.all_cards.sort(key=lambda card: card.value)

        less_than = True
        value_set = 4

        while value_set < 52:
            for card in new_deck.all_cards[:value_set]:
                for less_card in new_deck.all_cards[value_set:]:
                    if not card < less_card:
                        less_than = False
                        break

                if not less_than:
                    break

            value_set += 4

        self.assertTrue(less_than, f"{card} is less than {less_card}")

    def test_player_one_hand_count(self):
        '''Tests if Player One is dealt 26 cards at the start of the game'''

        new_game = war.War()
        self.assertEqual(len(new_game.player_one.all_cards), 26)

    def test_player_two_hand_count(self):
        '''Tests if Player Two is dealt 26 cards at the start of the game'''

        new_game = war.War()
        self.assertEqual(len(new_game.player_two.all_cards), 26)

    def test_player_hand_duplicates(self):
        '''Tests if a card is duplicated in both players' starting hands'''

        new_game = war.War()

        duplicate = False

        for card in new_game.player_one.all_cards:
            if card in new_game.player_two.all_cards:
                duplicate = True
                break

        self.assertFalse(duplicate, "Duplicate card found in both players' hands.")

    def test_out_of_cards(self):
        '''Tests if class method out_of_cards in War returns True for an empty hand'''

        new_game = war.War()

        new_game.player_one.all_cards.clear()

        self.assertTrue(war.War.is_out_of_cards(new_game.player_one), "Player is out of cards.")

    def test_out_of_cards_false(self):
        '''Tests if class method out_of_cards in War returns False for a player with at least
        one card'''

        new_game = war.War()

        self.assertFalse(war.War.is_out_of_cards(new_game.player_one))

if __name__ == '__main__':
    unittest.main()
