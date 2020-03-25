import pytest
import pandas as pd
import yaml

import sys
sys.path.append("..")
from covid19 import Covid19

def test_get_df_from_repo():
    with open("../config/config.yml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

    date = str(cfg["data"]["first_date"])
    covid19 = Covid19(cfg)
    df = covid19.get_df_from_repo(date)

    assert df["stato"][0] == "ITA"

def test_add_one_day():
    with open("../config/config.yml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

    date = str(cfg["data"]["first_date"])
    covid19 = Covid19(cfg)
    day = covid19.add_one_day(date)

    assert day == "20200225"

if __name__ == "__main__":
    test_add_one_day()

