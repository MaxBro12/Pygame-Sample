from sys import argv

from core import error_found, Game
from load_prof import main_check


def main(args: list = []):
    game = Game(main_check())
    game.run()


if __name__ == '__main__':
    try:
        if len(argv) > 1:
            main(argv[1:])
        main()
    except Exception as err:
        error_found(err)
