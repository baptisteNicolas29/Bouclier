from typing import List

from core.card import Card


class Player:

    def __init__(self, name:str) -> None:
        self.name = name
        self.__life = None
        self.__shield = []

    @property
    def life(self) -> Card:
        return self.__life

    @life.setter
    def life(self, card: Card) -> None:

        if isinstance(card, Card):
            self.__life = card

        else:
            raise TypeError('can not set life with {type(card)} need Card type')

    @property
    def shield(self) -> List[Card]:
        return self.__shield
