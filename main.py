from typing import List

from core import deck
from core import card


class Player:

    def __init__(self, name: str) -> None:

        self.__name = name

        self.__life: int = 0
        self.life_card: card.Card = None

        self.__shield: int = 0
        self.shield_cards: List[card.Card] = None


if __name__ == "__main__":

    deck1 = deck.Deck.generate_default_deck()
    deck2 = deck.Deck.generate_default_deck()

    deck1.shuffle()
    deck2.shuffle()

    new_deck = deck1 + deck2

    print(f'{new_deck = }')
    print(len(new_deck))

    for card in new_deck:
        print(card)
