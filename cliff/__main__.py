"""
cliff.__main__.py
~~~~~~~~~~~~~~~~~
"""
import readline

from cliff import __version__  # noqa
from cliff import data_io, user_interface as ui


def run():
    completer = ui.Completer(data_io.PLAYERS[:200])
    readline.set_completer(completer.complete)
    readline.parse_and_bind("tab: complete")

    while True:
        player_name = input("Player: ")
        print(data_io.info(player_name))


if __name__ == "__main__":
    run()
