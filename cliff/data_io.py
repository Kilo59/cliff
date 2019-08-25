"""
cliff.data_io.py
~~~~~~~~~~~~~~~~
"""
import pathlib

import pandas as pd

ROOT = pathlib.Path(__file__).parent.resolve()
DATA_SRC = ROOT / "cheatsheet.csv"
DATA = pd.read_csv(DATA_SRC)

if __name__ == "__main__":
    print(DATA_SRC)
    print(DATA.head())
    print(DATA["name"])

