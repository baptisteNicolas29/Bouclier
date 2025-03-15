

class Card(object):
    __doc__ = """
    Simple playing card object implementation for the Shield game.
    Card can hold a value and a color.
    It can also hold a head limit threshold,
    any value over this threshold is considered a head card.
    """

    head_threshold = 11

    # ASCII symbols for card colors
    color_symbols = {
        'clubs': '♣',
        'diamonds': '♦',
        'hearts': '♥',
        'spades': '♠',
    }

    def __init__(self, value: int, color: str) -> None:
        """
        Initialize Card object with a value and a color

        :param value: int, an integer value
        :param color: str, a string representing the color
        """
        self.__value = value
        self.__color = color

    @property
    def value(self) -> int:
        """
        The value of the card
        :return: int, representing the current value
        """
        return self.__value

    @property
    def color(self) -> str:
        """
        The color of the card
        :return: str, representing the color of the card
        """
        return self.__color

    @property
    def is_head(self) -> bool:
        """
        Whether the card if considered a head or not
        :return: bool, is the card a head
        """
        return self.__value >= Card.head_threshold

    def __str__(self) -> str:
        """
        String representation of the Card
        """
        error = f'SYMBOL NOT FOUND FOR COLOR -> {self.__color}'
        value, color = self.__value, self.color_symbols.get(self.__color, error)
        return f'{value} {color}'

    def __repr__(self):
        """
        String representation of the Card object
        """
        value, color = self.value, self.color
        return f'{self.__class__.__name__}({value}, "{color}")'


if __name__ == '__main__':

    card = Card(10, 'hearts')

    help(card)
    print(card.__repr__())
    print(card)
