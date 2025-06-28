from typing import List, AnyStr

from core import board


def main(player_names: List[AnyStr]) -> None:
    """
    Main function to start a game of Shield

    :param player_names: List[str], the list of player names
    """

    board.Board.start_a_game(player_names)


def launch_test_game() -> None:
    """
    Start a game of Shield with a list of TOTALLY random names
    """

    new_player_names: List[str] = [
        'lucas', 'julie', 'baptiste',
        'alan', 'olivier', 'morgane',
        'francois', 'coline'
    ]

    main(new_player_names)

if __name__ == "__main__":

    launch_test_game()
