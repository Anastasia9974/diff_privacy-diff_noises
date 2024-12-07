import pandas as pd

class GenerateData:
    def __init__(self, url):
        #'https://raw.githubusercontent.com/OpenMined/PyDP/dev/examples/Tutorial_4-Launch_demo/data/01.csv'
        self.url = url
        self.df1 = None
    def change_url(self, url):
        self.url = url
    def get_data(self):
        self.df1 = pd.read_csv(self.url, sep=",", engine="python")
    def print_data(self):
        print(self.df1.head())