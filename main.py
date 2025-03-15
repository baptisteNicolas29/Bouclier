from core import board


def main(player_names):
    """
    Main function to start a game of Shield

    :param player_names: List[str], the list of player names
    """

    board.Board.start_a_game(new_player_names)


if __name__ == "__main__":

    new_player_names = [
        'lucas', 'julie', 'baptiste',
        'alan', 'olivier', 'morgane',
        'francois'
    ]

    main(new_player_names)
