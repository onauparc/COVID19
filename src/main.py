import pandas as pd
import yaml

if __name__ == "__main__":
    # leggo il file di configurazione
    with open("../config/config.yml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

    url = 'https://raw.githubusercontent.com/lukes/ISO-3166-Countries-with-Regional-Codes/master/all/all.csv'
    df = pd.read_csv(url, index_col=0)
    print(df.head(5))