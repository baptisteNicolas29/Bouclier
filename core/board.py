from typing import List, Optional
import itertools
import random as rng

from core import deck
from core import player


class Board(object):
    __doc__ = """
    Simple Board object implementation for the Shield game.
    
    The Board manages the game setup, the game start and player turn tracking.
    Each turn it asks the current player which action they would like to perform
    and then executes the chosen action before moving on to the next player and
    repeating the process. The game ends when only one player remains.
    """

    # default player actions for the game
    __default_actions = ['Attack', 'Charge', 'Swap', 'Custom']

    @classmethod
    def start_a_game(
            cls, 
            player_names: List[str], 
            custom_deck: Optional[deck.Deck] = None
    ) -> None:
        """
        Set up the game and starts the game loop, given player names

        :param player_names: List[str], the list of player names
        :param custom_deck: Optional[deck.Deck], a Deck to play the game
        """
        players = []
        for player_name in player_names:
            players.append(player.Player(player_name))

        rng.shuffle(players)

        board = cls(players, custom_deck=custom_deck)
        board.turn_tracker = 0
        board.distribute_health_card_to_all_players()
        board.distribute_shield_cards_to_all_players()

        while len(board.players) > 1:
            board.take_turn()
        else:
            last_player = board.players[0].name
            print(f'WINNER IS {last_player.upper()}, CONGRATULATIONS!')

    def __init__(
            self,
            players : List[player.Player],
            custom_deck: Optional[deck.Deck] = None
    ) -> None:
        """
        Initialize a Board object given Players

        :param players: List[player.Player], a list of Players to play the game
        :param custom_deck: Optional[deck.Deck], a Deck to play the game
        """

        # Assert all players are of type player.Player
        assert all(isinstance(p, player.Player) for p in players), (
            f'Board expected List[player.Player], '
            f'\n\tGOT {[p.__class__.__name__ for p in players]}'
        )
        # Assert custom Deck is of type deck.Deck or None
        assert isinstance(custom_deck, Optional[deck.Deck]), (
            f'Board expected deck.Deck or None, \n\tGOT {type(custom_deck)}'
        )

        self.__turn_tracker = itertools.cycle(list(range(len(players))))

        self.__players = players
        self.__current_player = None

        self.__deck = custom_deck or deck.Deck.generate_default_deck()
        self.__deck.shuffle()

        self.__discard_pile = deck.Deck()

    @property
    def players(self) -> List[player.Player]:
        """
        The list of Players still in the game

        :return: List[player.Player], the list of players in the game
        """
        return self.__players

    @property
    def current_player(self) -> player.Player:
        """
        The Player whose turn it is

        :return: player.Player, the Player currently playing
        """
        return self.__current_player

    @property
    def deck(self) -> deck.Deck:
        """
        The Deck used for the current game

        :return: deck.Deck, the current Deck
        """
        return self.__deck

    def show_player_infos(self) -> None:
        """
        Prints the Players' visible information

        For each player still in the game, shows the name, life value,
        life card, shield value and shield cards
        """
        print(f'{"-" * 10}')

        show_info = input('Show Player Infos? (Y/N) :')
        if not show_info.lower() =='y':
            f'\n{"-" * 10}'
            return

        for current_player in self.players:
            current_player.show_info()

    # distribute cards to players
    def distribute_health_card_to_all_players(self) -> None:
        """
        Distributes Cards to all Players in the current game to serve as health
        """

        for player_obj in self.__players:
            self.distribute_health_card(player_obj)

    def distribute_health_card(self, player_obj: player.Player) -> None:
        """
        Distributes Cards to a  given Players to serve as health

        :param player_obj: : player.Player, a Player to distribute a Card to
        """

        player_obj.life_card = self.__deck.draw()

    def distribute_shield_cards_to_all_players(self) -> None:
        """
        Distributes Cards to all Players in the current game to serve as shield
        """

        for player_obj in self.__players:
            self.distribute_shield_cards(player_obj)

    def distribute_shield_cards(self, player_obj: player.Player) -> None:
        """
        Distributes Cards to a  given Players to serve as shield

        :param player_obj: : player.Player, a Player to distribute Cards to
        """

        player_obj.shield_cards = [self.__deck.draw() for _ in range(2)]

    # GAME ACTIONS
    def attack(self, player1: player.Player, player2: player.Player) -> None:
        """
        Perform the Attack action from one Player to another

        If the attack is higher than the shield value then the life is affected,
        If life is affected then new shield Cards are distributed to the
        attacked Player.
        :param player1: player.Player, the attacking Player.
        :param player2: player.Player, the attacked Player.
        """

        # Count the attack value
        attack_card = self.deck.draw()
        charged_value = player1.charge
        attack_value = attack_card.value + charged_value
        player1.reset_charges()

        print(
            f'{player1.name.upper()} attacking '
            f'{player2.name.upper()} for {attack_value}'
        )
        # Count the remainder after shield calculations
        remainder = player2.shield - attack_value
        print(
            f' -> Hit {player2.name.upper()}\'s Shield: {player2.shield} '
            f'- {attack_value} = {remainder}'
        )

        if remainder > 0:
            player2.shield = remainder

        else:
            life_copy = player2.life
            player2.life += remainder

            print(
                f' -> Hit Life : {life_copy} - {-remainder} = {player2.life}'
            )

            player2.reset_charges()

            self.distribute_shield_cards(player2)
            print(f' -> {player2.life = }\n- {player2.shield = }')

    def charge(self, player1: player.Player) -> None:
        """
        Perform the charge action for given Player

        Draws a Card and add it to the Player's charged_cards
        All charged Cards are used if the Player Atacks
        All charges are lost when the Player looses life

        :param player1: player.Player, the Player charging an attack Card
        """
        print(f'{player1.name.upper()} is charging an attack card')
        player1.charged_cards = self.deck.draw()

    def swap(self, player1: player.Player, player2: player.Player) -> None:
        """
        Perform the swap action for given Player.

        Swap changes one of the shield Cards of a Player,
        it can be used to change the current Player's shield

        :param player1: player.Player, the swapping Player.
        :param player2: player.Player, the swapped Player.
        """
        swap_card = self.deck.draw()

        copy_cards = player2.shield_cards.copy()
        swap_mssg = '\n\t'.join(
            f'-> {k}-{v}' for k, v in enumerate(copy_cards)
        )

        card_choice = int(input(
            f'Choose a shield card to swap:\n\t{swap_mssg}\nChoice:'
        ))
        print(
            f'{player1.name.upper()} is swapping {player2.name.upper()} shield:'
            f'\n\tFrom {copy_cards[card_choice]} to {swap_card}'
        )
        new_shield = []
        for i, card in enumerate(player2.shield_cards):
            if i == card_choice:
                new_shield.append(swap_card)
            else:
                new_shield.append(player2.shield_cards[i])

        player2.shield_cards = new_shield

    # GAME LOOP
    def choose_player(
            self,
            player1: player.Player,
            full: bool = False
    ) -> player.Player:
        """
        Choose a Player from the current Player list

        :param player1: player.Player, the Player making the choice
        :param full: bool, whether to include the current Player in the choice
        :return: player.Player, the chosen Player
        """
        player_copy = self.players.copy()

        if not full:
            player_copy.remove(player1)

        player_mssg = '\n\t'.join(
            f'-> {k}-{v.name}' for k, v in enumerate(player_copy)
        )
        player_choice = input(
            f'Choose an opponent :\n\t{player_mssg}\nChoice:'
        )
        return player_copy[int(player_choice)]

    def update_players(self, player_index: int) -> None:
        """
        Update Player's list at the end of a turn if an update is needed

        If a Player has a life total less than 0, they are removed from the game
        Updates the __turn_tracker
        :param player_index: int, the current Player index
        """

        is_before = True
        for i, player_obj in enumerate(reversed(self.__players)):

            if i > player_index:
                is_before = False

            if player_obj.life > 0:
                continue

            print(f'PLAYER KILLED: {player_obj.name}')
            self.__players.remove(player_obj)

        player_index -= 1 if is_before else 0
        self.__turn_tracker = itertools.cycle(list(range(len(self.__players))))

        for i in range(player_index+1):
            next(self.__turn_tracker)

    def choose_action(self) -> bool:
        """
        Choose the action for the current Player turn

        :return bool, whether the Player list needs an update after an attack
        """
        action_mssg = f'\n\t'.join(
            f'-> {k}-{v}' for k, v in enumerate(self.__default_actions)
        )

        action = int(input(
            f'\n{self.current_player.name} - '
            f'Choose an action number :\n\t{action_mssg}\nChoice:'
        ))

        need_update = False
        if action == 0:  # attack
            attacked_player = self.choose_player(self.current_player)
            self.attack(self.current_player, attacked_player)
            need_update = attacked_player.life <= 0

        elif action == 1:  # charge
            self.charge(self.current_player)

        elif action == 2:  # swap shield
            swap_player = self.choose_player(self.current_player, full=True)
            self.swap(self.current_player, swap_player)

        elif action == 3:
            print('NO CUSTOM ACTIONS, CHOOSE AGAIN...')
            return self.choose_action()

        return need_update

    def take_turn(self) -> None:
        """
        Process the turn of the current Player
        """
        self.show_player_infos()

        current_player_index = next(self.__turn_tracker)
        self.__current_player = self.players[current_player_index]

        need_update = self.choose_action()

        if need_update:
            self.update_players(current_player_index)


if __name__ == "__main__":

    new_player_names = [
        'lucas', 'julie', 'baptiste',
        'alan', 'olivier', 'morgane',
        'francois'
    ]

    rng.shuffle(new_player_names)
    Board.start_a_game(new_player_names)
