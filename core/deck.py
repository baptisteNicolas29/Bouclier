import random as rng
from typing import List, Optional

from core import card


class Deck(object):
    __doc__ = """
    Simple deck of cards object implementation for the Shield game.
    
    Deck cn hold Cards and a discard pile
    It is initialize through class methods
        -> generate_default_deck(), for a classic 52 card deck
        -> generate_deck(value_range, color_list), for a custom deck
    """

    __default_range = range(1, 14)
    __default_colors = ['spades', 'clubs', 'hearts', 'diamonds']

    @classmethod
    def generate_default_deck(cls) -> 'Deck':
        """
        Generates a standard 52 card deck

        :return: Deck, and instance of the object
        """

        return Deck.generate_deck(cls.__default_range, cls.__default_colors)

    @classmethod
    def generate_deck(
            cls,
            value_range: range | List[int],
            color_list: List[str]
    ) -> 'Deck':
        """
        Generate a Deck object using given values and colors

        :param value_range: range, the range of values for each color
        :param color_list: list[str], the list of colors for the new deck

        :return: Deck, and instance of the object
        """

        cards = [
            card.Card(value, color)
            for color in color_list
            for value in value_range
        ]

        return cls(cards)

    def __init__(self, cards: Optional[List[card.Card]] = None) -> None:
        """
        Initialize Deck object

        Use class methods to initialize a Deck
        """
        self.__cards = cards or []
        self.__discard_pile = []

    @property
    def cards(self) -> List[card.Card]:
        """
        The Cards in the current Deck

        :return: List[card.Card], list of Cards in the card pile
        """
        return self.__cards

    @cards.setter
    def cards(self, card_list: List[card.Card]) -> None:
        """
        Setter for the cards property

        :param card_list: List[card.Card], list of Card objects
        """
        if not isinstance(card_list, List):
            raise TypeError(f'Cards must be a list, got {type(card_list)} instead, aborting...')

        self.__cards = card_list

    @property
    def discard_pile(self) -> List[card.Card]:
        """
        A list a Cards no longer in the current Deck

        :return: List[card.Card], list of Cards in the discard_pile
        """
        return self.__discard_pile

    @discard_pile.setter
    def discard_pile(self, card_list: List[card.Card]) -> None:
        """
        Setter for the discard_pile property

        :param card_list: List[card.Card], a list of Card objects
        """
        if not isinstance(card_list, List):
            raise TypeError(
                f'Discard Pile must be a list, got {type(card_list)} instead, '
                f'aborting...'
            )

        self.__discard_pile = card_list

    def discard(self, item: card.Card) -> None:
        """
        Add a given Card to the discard_pile

        :param item: card.Card, the card to discard
        """
        self.__discard_pile.append(item)

    def shuffle(self) -> List[card.Card]:
        """
        Shuffles the card_pile

        :return: list[card.Card], the shuffled card pile
        """
        rng.shuffle(self.__cards)
        return self.__cards

    def draw(self, cycle: bool = True) -> card.Card:
        """
        Draws a Card from the card_pile,

        Can shuffle the discard_pile in the card_pile
        if the latter has no Cards left

        :param cycle: bool, whether to cycle cards if none are left in card_pile
        :return: card.Card, the drawn Card
        """

        # cycle drawable cards from the discard pile
        if len(self.__cards)==0 and cycle:
            self.__cards = self.__discard_pile.copy()
            self.__discard_pile.clear()
            self.shuffle()

        item = self.__cards.pop(0)
        self.__discard_pile.append(item)

        return item

    def put_top(self, item: card.Card) -> None:
        """
        Insert a card at index 0 of the card pile

        :param item: card.Card, the Card object to insert
        """
        self.insert(item)

    def append(self, item: card.Card) -> None:
        """
        Append the given Card object to the current Deck

        :param item: card.Card, the card to append to the Deck
        """
        self.__cards.append(item)

    def insert(self, item: card.Card, index: int = 0) -> None:
        """
        Insert a Card in the current deck at the given index (default is 0)

        :param item: card.Card, the Card object to insert in the Deck
        :param index: int, index at which to inset the given Card, default is 0
        """
        self.__cards.insert(index, item)

    def remove_value(self, value: int) -> None:
        """
        Remove all card with the given value from the Deck object

        :param value: int, the value of the card to remove
        """
        for i, item in reversed(list(enumerate(self.__cards))):
            if item.value == value:
                self.__cards.pop(i)

    def remove_color(self, color: str) -> None:
        """
        Remove all card with the given color from the Deck object

        :param color: str, the color of the card to remove
        """
        for i, item in reversed(list(enumerate(self.__cards))):
            if item.color == color:
                self.__cards.pop(i)

    def remove_card(self, value: int, color: str) -> None:
        """
         Remove a card from the Deck object

        :param value: int, the value of the card to remove
        :param color: str, the color of the card to remove
        """
        for i, item in reversed(list(enumerate(self.__cards))):
            if item.color == color and item.value == value:
                self.__cards.pop(i)

    def __add__(self, other: 'Deck') -> 'Deck':
        """
        Adds two Deck objects together using cards and discard_pile

        :param other: Deck, the second Deck to add
        :return: Deck, the resulting Deck object
        """
        new_deck = Deck()
        new_deck.cards = self.cards + other.cards
        new_deck.discard_pile = self.discard_pile + other.discard_pile

        return new_deck

    def __iter__(self) -> card.Card:
        """
        Make Deck object iterable, iterate through cards and yields them

        :return: card.Card, the current Card in the iteration
        """
        for item in self.__cards:
            yield item

    def __len__(self) -> int:
        """
        The length of the Deck

        :return: int, the number of cards in the Deck
        """
        return len(self.__cards)

    def __str__(self) -> str:
        """
        Representation of the Deck

        :return: str, string representing the current Deck
        """
        card_pile, discard_pile = len(self.__cards), len(self.__discard_pile)
        return f'Deck - {card_pile=}, {discard_pile=}'

    def __repr__(self) -> str:
        """
        Representation of the Deck object

        :return: str, string representing the current Deck object
        """
        card_pile, discard_pile = self.__cards, self.__discard_pile
        repr_str = (
            f'deck = {self.__class__.__name__}()'
            f'\ndeck.{card_pile = }'
            f'\ndeck.{discard_pile = }'
        )
        return repr_str


if __name__ == '__main__':

    deck = Deck.generate_default_deck()
    # values = [i for i in range(1, 20, 2)]
    # colors = [str(i) for i in range(0, 4)]
    # deck = Deck.generate_deck(values, colors)

    help(deck)
    print(deck.__repr__())
    print(deck)

