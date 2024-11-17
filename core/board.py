from core import deck


class Board:

    def __init__(self) -> None:
        self.__draw = deck.Deck()
        self.__discard = deck.Deck()
        self.__players = []

