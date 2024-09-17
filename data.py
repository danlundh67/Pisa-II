import pandas as pd
from constants import PISA_PATH


class Pisa:
    def __init__(self):
        self.df = pd.read_csv(PISA_PATH)

class PisaData(Pisa):
    def __init__(self):
        super().__init__()
        self.df = self.df

    @property
    def data(self):
        return self.df

class GetBasics():
    def __init__(self):
        self.df = PisaData().data

    @property
    def data(self):
        return self.df
    
    @property
    def numbcontries(self):
        return len(self.df['LOCATION'].unique())
    
    @property
    def therows(self):
        return self.df['LOCATION'].count()
    
    @property
    def subjects(self):
        return len(self.df['INDICATOR'].unique())



class AvgCountry():
    def __init__(self) -> None:
        self.df_avg_contry = PisaData().data

    @property
    def score_contry(self):
        averge = (
            self.df_avg_contry.groupby(by=['LOCATION', 'INDICATOR'])['Value'].mean().unstack().reset_index(names='LOCATION')
        )

        return averge

if __name__ == "__main__":
    df = Pisa().data
    print(df)