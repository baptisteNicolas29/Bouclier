

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
        return self.__value > 10

    def __str__(self) -> str:
        return f'{self.__value} {self.__color}'
