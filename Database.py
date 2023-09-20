from Stars import Stars
import pandas as pd

class Database:

    starsDf = 0
    stars = []

    def import_statistics(self):
        self.starsDf = pd.read_excel("projectedstats.xlsx")


    def __init__(self):
        self.import_statistics()
        self.starsDf = self.starsDf[self.starsDf["POS"] != "POS"]



        for row in self.starsDf.itertuples():
            self.stars.append(Stars(row))
        


    


