import pandas as pd
import yaml
import logger
import datetime
from datetime import timedelta
import os

class Covid19:
    def __init__(self, cfg):
        self.cfg = cfg
        self.logger = logger.get_logger(os.path.realpath(__file__)+"/../log/"+cfg["logging"]["filename"], cfg["logging"]["level"])

    def get_df_from_repo(self, date):
        """
        get df of a specific date from the repo
        :param date: date
        :return: df
        """
        try:
            url = self.cfg["data"]["repo"] + self.cfg["data"]["filename"] + date + "." + self.cfg["data"]["extension"]
            df = pd.read_csv(url)
            return df
        except Exception as e:
            self.logger.error(e, exc_info=True)

    def add_one_day(self, date):
        """
        the function add a day to a date
        :param date: date
        :return: date one day after
        """
        format = '%Y%m%d'
        date_datetime = datetime.datetime.strptime(date, format)
        new_date = date_datetime + timedelta(days=1)
        return new_date.strftime(format)


    def get_all_df(self):
        """
        get all the df on the repo
        :return: lisf of df
        """
        first_date_str = str(cfg["data"]["first_date"])
        pass

    def make_analysis(self):
        pass

if __name__ == "__main__":
    # leggo il file di configurazione
    with open("../config/config.yml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

    covid19 = Covid19(cfg)