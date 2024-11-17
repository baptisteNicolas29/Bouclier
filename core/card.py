from typing import Optional, Union


class Card:

    def __init__(self, value: int, color: str) -> None:
        self.__value = value
        self.__color = color

    @property
    def value(self) -> int:
        return self.__value

    @property
    def color(self) -> str:
        return self.__color

    @property
    def is_head(self) -> bool:
        return self.__value >= 10

    def is_same(self, other) -> bool:

        if not isinstance(other, Card):
            return False

        for attr in ['value', 'color']:
            if getattr(self, attr) != getattr(other, attr):
                return False

        else:
            return True

    def __str__(self) -> str:
        return f'{self.__value} {self.__color}'

    def __add__(self, other: Union['Card', int]) -> Union['Card', int]:

        if isinstance(other, int):
            return self.__value + other

        elif isinstance(other, Card):
            return self.__class__(
                    self.value + other.value,
                    self.__color
                    )

        else:
            raise NotImplementedError(
                    f'Card can be added to Card or int not {type(other)}'
                    )

    def __sub__(self, other: Union['Card', int]) -> Union['Card', int]:

        if isinstance(other, int):
            return self.__value - other

        elif isinstance(other, Card):
            return self.__class__(
                    self.value - other.value,
                    self.__color
                    )

        else:
            raise NotImplementedError(
                    f'Card can be added to Card or int not {type(other)}'
                    )

    def __eq__(self, other: Union['Card', int]) -> bool:

        if isinstance(other, int):
            return self.__value == other

        elif isinstance(other, Card):
            return self.__value == other.value

    def __gt__(self, other: Union['Card', int]) -> bool:

        if isinstance(other, int):
            return self.__value > other

        elif isinstance(other, Card):
            return self.__value > other.value

    def __lt__(self, other: Union['Card', int]) -> bool:

        if isinstance(other, int):
            return self.__value < other

        elif isinstance(other, Card):
            return self.__value < other.value

    def __ge__(self, other):
        return (self > other) | (self == other)

    def __le__(self, other):
        return (self < other) | (self == other)
