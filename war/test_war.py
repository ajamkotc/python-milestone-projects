import unittest
import war

class TestWar(unittest.TestCase):

    def test_deck_length(self):
        '''Tests if 52 cards are generated when a new Deck is formed'''

        new_deck = war.Deck()
        self.assertEqual(len(new_deck), 52, "Deck does not contain 52 cards")

    def test_deck_unique(self):
        '''Tests if there are any duplicates in the Deck'''

        new_deck = war.Deck()
        duplicate = False

        index = 0

        while index < 52 and duplicate == False:
            bottom_card = new_deck.deal_one()
            duplicate = bottom_card in new_deck.all_cards

            index += 1

        self.assertFalse(duplicate, f"Duplicate found: {bottom_card}")

    def test_card_gt(self):
        new_deck = war.Deck()
        new_deck.all_cards.sort(key=lambda card: card.value)

        greater_than = False

        for card in new_deck.all_cards[:4]:
            for greater_card in new_deck.all_cards[4:]:
                if card > greater_card:
                    greater_than = True

        self.assertFalse(greater_than, "Lower valued card greater than greater valued")

    def test_card_lt(self):
        new_deck = war.Deck()
        new_deck.all_cards.sort(key=lambda card: card.value)

        less_than = True

        for card in new_deck.all_cards[:4]:
            for less_card in new_deck.all_cards[4:]:
                if card > less_card:
                    less_than = False

        self.assertTrue(less_than, "Greater valued card ")

if __name__ == '__main__':
    unittest.main()