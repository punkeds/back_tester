import pandas as pd
import mysql.connector as MySQL

from data_handler import DataHandler

def DataPrepare():
    connection = MySQL.connect(host='localhost', database='exchange', user='root', password='mysql')

    Si = DataHandler('Si', '2015-08-01', '2015-11-06', connection)

    SiSMA5High = Si.SMA(5, '5Min', 'high')
    SiSMA5Low = Si.SMA(5, '5Min', 'low')
    Si5 = Si.SetTimeFrame('5Min')

    InputData = pd.merge(Si5, SiSMA5High, how='inner', left_index=True, right_index=True)
    InputData = pd.merge(InputData, SiSMA5Low, how='inner', left_index=True, right_index=True)

    return InputData

