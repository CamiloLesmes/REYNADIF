import pandas as pd
import random
import matplotlib.pyplot as plt
from Codigo1 import CapturaDatos
from MongoClass import MongoClass

class PrepareData:

    def __init__(self):
        self.listReturned = CapturaDatos()
        self.listData = []

    def prepareJson(self):
        self.listReturned.Captura()
        self.listData = self.listReturned.limpieza()

    def storeDataPrepared(self):
        capture = MongoClass()
        print(capture.storeDataMany(self.listData))

    def monthChoise(self,quarter):
        months = {
            1: ['January', 'February', 'March'],
            2: ['April', 'May', 'June'],
            3: ['July', 'August', 'September'],
            4: ['October', 'November', 'December']
        }
        return random.choice(months.get(quarter))

    def pandasDataPrepared(self):
        df = pd.DataFrame(self.listData,columns=['Year','Quarter','Provider','Income','amountSMS'])
        df['Quarter'] = df['Quarter'].astype(int)
        df['Month'] = df['Quarter'].apply(self.monthChoise)
        df['Month_Num'] = df['Month'].map({
            'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
            'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12
        })

        X = df[['Year','Quarter','amountSMS','Month_Num']]
        Y = df['Income']



prueba = PrepareData()
prueba.prepareJson()
prueba.pandasDataPrepared()
