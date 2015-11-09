import pandas as pd
import mysql.connector as MySQL

from data_handler import DataHandler
from strategy import Signal

# ##
# Data preparation
###

connection = MySQL.connect(host='localhost', database='exchange', user='root', password='mysql')

Si = DataHandler('Si', '2015-08-01', '2015-11-06', connection)

SiSMA5High = Si.SMA(5, '5Min', 'high')
SiSMA5Low = Si.SMA(5, '5Min', 'low')
Si5 = Si.SetTimeFrame('5Min')

InputData = pd.merge(Si5, SiSMA5High, how='inner', left_index=True, right_index=True)
InputData = pd.merge(InputData, SiSMA5Low, how='inner', left_index=True, right_index=True)


#print(InputData.head(10))
OrdersLine = {'datetime': [],
              'type': [],
              'open_price': [],
              'close_price': [],
              'profit': []
              }
State = {'state': 'close'}
for datetime in InputData.index:
    #print(InputData.loc[datetime][['low', 'high']])
    Orders = Signal(InputData.loc[datetime])
    #print(Orders)

    if State['state'] == 'open' and State['stop_loss_price'] >= InputData.loc[datetime]['low'] and State['stop_loss_price'] <= InputData.loc[datetime]['high']:
            OrdersLine['datetime'].append(datetime)
            OrdersLine['type'].append(State['type'])
            OrdersLine['open_price'].append(State['open_price'])
            OrdersLine['close_price'].append(State['stop_loss_price'])
            if State['type'] == 'buy':
                profit = State['stop_loss_price'] - State['open_price']
            else:
                profit = State['open_price'] - State['stop_loss_price']
            OrdersLine['profit'].append(profit)
            State = {'state': 'close'}


    for Order in Orders:
        if State['state'] == 'close':
            State = {
                'state': 'open',
                'type': Order['type'],
                'open_price': Order['price'],
                'stop_loss_price': Order['stop_loss_price']
            }
        elif State['type'] != Order['type']:
            OrdersLine['datetime'].append(datetime)
            OrdersLine['type'].append(State['type'])
            OrdersLine['open_price'].append(State['open_price'])
            OrdersLine['close_price'].append(Order['price'])
            if State['type'] == 'buy':
                profit = Order['price'] - State['open_price']
            else:
                profit = State['open_price'] - Order['price']
            OrdersLine['profit'].append(profit)
            State = {'state': 'close'}




OrdersLine = pd.DataFrame(OrdersLine)
OrdersLine = OrdersLine.set_index(['datetime'])

OrdersLine = OrdersLine['profit'].resample("1D", how="sum")
OrdersLine.to_csv('one.csv')
print(OrdersLine)
#OrdersLine = OrdersLine[(InTimeFrame.vol >= 0)]