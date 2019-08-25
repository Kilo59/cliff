"""
cliff.data_io.py
~~~~~~~~~~~~~~~~
"""
import pathlib

import pandas as pd

ROOT = pathlib.Path(__file__).parent.resolve()
DATA_SRC = ROOT / "cheatsheet.csv"
DATA = pd.read_csv(DATA_SRC)
PLAYERS = DATA["player_name"].str.strip()
DATA.update(PLAYERS)


def info(player_name):
    player_data = DATA.loc[DATA["player_name"] == player_name]
    return f"\t{player_data['price'][0]}\tBYE: {player_data['bye'][0]}"
