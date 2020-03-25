import pandas as pd
import yaml

class Covid19:
    def __init__(self, cfg):
        self.cfg = cfg

    def get_df_from_repo(self, date):
        url = self.cfg["data"]["repo"] + self.cfg["data"]["filename"] + date + "." + self.cfg["data"]["extension"]
        df = pd.read_csv(url)
        return df

    def get_all_df(self):
        pass

    def make_analysis(self):
        pass

if __name__ == "__main__":
    # leggo il file di configurazione
    with open("../config/config.yml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

    covid19 = Covid19(cfg)