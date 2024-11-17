import random as rng

from core import card


class Deck:

    @classmethod
    def generate_default_deck(cls) -> None:
        deck = cls()

        for color in ['spades', 'clubs', 'hearts', 'diamonds']:
            for value in range(1, 14):
                deck.append(card.Card(value, color))

        return deck

    def __init__(self) -> None:
        self.__cards = []

    def __len__(self) -> int:
        return len(self.__cards)

    def shuffle(self) -> None:
        rng.shuffle(self.__cards)
        return self.__cards

    def pick(self) -> card.Card:
        return self.__cards.pop(0)

    def put_top(self, card: card.Card) -> None:
        self.__cards.insert(0)

    def append(self, card: card.Card) -> None:
        self.__cards.append(card)

    def insert(self, index: int, card: 'card.Card') -> None:
        self.__cards.insert(index, card)

    def __add__(self, other) -> 'Deck':
        return self + other

    def __iter__(self):
        for item in self.__cards:
            yield item

    def __contains__(self, card: 'card.Card') -> bool:
        return card in self.__cards

    def __getitem__(self, index: int) -> 'card.Card':
        return self.__cards[index]
