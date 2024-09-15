import pandas as pd
from constants import PISA_PATH


class Pisa:
    def __init__(self):
        self.df = pd.read_csv(PISA_PATH)