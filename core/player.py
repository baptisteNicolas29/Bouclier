from typing import List

from core import card

class Player:
    __doc__ = """
    Simple player object implementation for the Shield game.
    
    Player is defined by a name, life total and life card,
    shield total and shield cards as well as charged total and charged cards
    """

    def __init__(self, name: str) -> None:
        """
        Initialize a Player object

        :param name: str, the name of the new player
        """

        self.__name = name.capitalize()

        self.__life: int = 0
        self.__life_card: card.Card | None = None

        self.__shield: int = 0
        self.__shield_cards: List[card.Card] = []

        self.__charge: int = 0
        self.__charged_cards: List[card.Card] = []

    @property
    def name(self) -> str:
        """
        The name of the current player

        :return: str, the name of the player
        """
        return self.__name

    @property
    def life(self) -> int:
        """
        The value that serves as life total

        :return: int, the total life value
        """
        return self.__life

    @life.setter
    def life(self, value: int) -> None:
        """
        The setter for the life property

        :param value: int, the value serving as life total
        """
        self.__life = value

    @property
    def life_card(self) -> card.Card:
        """
        The Card serving as life total

        :return: card.Card, the Card serving as life total
        """
        return self.__life_card

    @life_card.setter
    def life_card(self, item: card.Card) -> None:
        """
        The setter for the life_card property

        Set the current life_total Card

        :param item: card.Card, the Card serving as life total
        """
        self.__life_card = item
        self.__life = item.value

    @property
    def shield(self) -> int:
        """
        The current value representing the shield

        :return: int,  the value of the current shield
        """
        return self.__shield

    @shield.setter
    def shield(self, value: int) -> None:
        """
        The setter for the shield property

        :param value: int, The value of the new shield
        """
        self.__shield = value

    @property
    def shield_cards(self) -> List[card.Card]:
        """
        The list of Cards used to shield the player against attacks

        :return: List[card.Card], a list of Cards that serve as shield_cards
        """
        return self.__shield_cards

    @shield_cards.setter
    def shield_cards(self, items: List[card.Card]) -> None:
        """
        The setter for the shield_cards property

        Also sets the shield property

        :param items: List[card.Card], a list of Cards to serve as shield_cards
        """
        self.__shield_cards = items
        self.__shield = sum(item.value for item in items)

    @property
    def charge(self) -> int:
        """
        The sum of all currently charged Cards

        :return: int, the charged value
        """
        return self.__charge

    @property
    def charged_cards(self) -> List[card.Card]:
        """
        A list of all the cards currently charged by the player

        :return: List[card.Card], the list of charged Cards
        """
        return self.__charged_cards

    @charged_cards.setter
    def charged_cards(self, item: card.Card) -> None:
        """
        Setter for the charged_cards property

        Add the given Card to the charged attack

        :param item: card.Card, the charged Card
        """
        self.__charged_cards.append(item)
        self.__charge += item.value

    def reset_charges(self) -> None:
        """
        Reset the currently held charged attacks
        """
        self.__charged_cards = []
        self.__charge = 0

    def show_info(self) -> List:
        """
        Prints the Player's visible information

        Shows the name, life value, life card, shield value and shield cards
        :return list, list holding the player's current information
        """

        player_data = [
            self.name,
            self.life, self.life_card,
            self.shield, self.shield_cards
        ]
        print(
            f'Player Name : {self.name}'
            f'\n\tLife : {self.life} - {self.life_card}'
            f'\n\tShield : [ {self.shield} ] -> '
            f'{[str(shield_card) for shield_card in self.shield_cards]}'
            f'\n\tCharged Attacks: {len(self.charged_cards)}'
            
            f'\n{"-" * 10}'
        )
        return player_data

    def __str__(self):
        """
        Representation of the Player

        :return: str, string representing the current Player
        """

        player_string = (
            f"Player - name={self.name}, "
            f"life={self.life}, life_cards={self.life_card}, "
            f"shield={self.shield}, shield_cards={self.shield_cards}"
            f"charge={self.charge}, charged_cards={self.charged_cards}"
        )

        return player_string

    def __repr__(self):
        """
        Representation of the Player object

        :return: str, string representing the current Player object
        """

        life_card = self.life_card
        shield_cards = self.shield_cards
        charged_cards = self.charged_cards
        repr_str = (
            f'player = {self.__class__.__name__}({self.name})'
            f'\nplayer.{life_card = }'
            f'\nplayer.{shield_cards = }'
            f'\nplayer.{charged_cards = }'
        )
        return repr_str


if __name__ == '__main__':

    player = Player('Lucas')

    help(player)
    print(player.__repr__())
    print(player)