from typing import List

from core.player import Player
from core import deck


class Board:

    def __init__(self) -> None:

        self.__draw = deck.Deck()
        self.__discard = deck.Deck()
        self.__players = []

    @property
    def players(self) -> List[Player]:
        return self.__players
