from typing import List

from core import deck
from core import card


class Player:

    def __init__(self, name: str) -> None:

        self.__name = name

        self.__life: int = None
        self.life_card: card.Card = None
        self.__shilds: List[card.Card] = None


if __name__ == "__main__":

    cards = deck.Deck.generate_default_deck()
    # cards.shuffle()

    for card in cards:
        print(card)
