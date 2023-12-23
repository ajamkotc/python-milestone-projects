import unittest
import blackjack
import random

class TestBlackjack(unittest.TestCase):
    def test_deck_length(self):
        '''Tests the length of the deck.'''

        new_deck = blackjack.Deck()
        self.assertEqual(len(new_deck.all_cards), 52, f"Deck has {len(new_deck.all_cards)}")

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

        self.assertEqual(len(new_deck.all_cards), 52 - random_rep)

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

if __name__ == '__main__':
    unittest.main()
