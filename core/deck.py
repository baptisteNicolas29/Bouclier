import random as rng
from typing import List

from core import card


class Deck:

    @classmethod
    def generate_default_deck(cls) -> 'Deck':
        deck = cls()

        value_range = range(1, 14)
        color_list = ['spades', 'clubs', 'hearts', 'diamonds']

        return deck.generate_deck(value_range, color_list)

    @classmethod
    def generate_deck(cls, value_range: range, color_list: List[str]):
        """

        :param value_range:
        :param color_list:
        :return:
        """
        deck = cls()

        for color in color_list:
            for value in value_range:
                deck.append(card.Card(value, color))

        return deck

    def __init__(self) -> None:
        self.__cards = []
        self.__discard_pile = []

    @property
    def cards(self):
        return self.__cards

    @cards.setter
    def cards(self, card_list):
        if not isinstance(card_list, List):
            raise TypeError(f'Cards must be a list, got {type(card_list)} instead, aborting...')

        self.__cards = card_list

    @property
    def discard_pile(self):
        return self.__discard_pile

    @discard_pile.setter
    def discard_pile(self, card_list):
        if not isinstance(card_list, List):
            raise TypeError(f'Discard Pile must be a list, got {type(card_list)} instead, aborting...')

        self.__discard_pile = card_list

    def shuffle(self) -> List[card.Card]:
        rng.shuffle(self.__cards)
        return self.__cards

    def draw(self) -> card.Card:
        item = self.__cards.pop(0)
        self.__discard_pile.append(item)

        return item

    def put_top(self, item: card.Card) -> None:
        self.__cards.insert(0, item)

    def append(self, item: card.Card) -> None:
        self.__cards.append(item)

    def insert(self, index: int, item: 'card.Card') -> None:
        self.__cards.insert(index, item)

    def remove_value(self, value):
        for i, item in reversed(list(enumerate(self.__cards))):
            if item.value == value:
                self.__cards.pop(i)

    def remove_color(self, color):
        for i, item in reversed(list(enumerate(self.__cards))):
            if item.color == color:
                self.__cards.pop(i)

    def remove_card(self, value, color):
        for i, item in reversed(list(enumerate(self.__cards))):
            if item.color == color and item.value == value:
                self.__cards.pop(i)

    def __add__(self, other) -> 'Deck':
        new_deck = Deck()
        new_deck.cards = self.cards + other.cards
        new_deck.discard_pile = self.discard_pile + other.discard_pile

        return new_deck

    def __iter__(self):
        for item in self.__cards:
            yield item

    def __len__(self):
        return len(self.__cards)
