import pandas as pd

class DataHandler(object):

    def __init__(self, Instrument, DateFrom, DateTo, Connection):
        SqlQuery = "SELECT * FROM " + Instrument + " "\
                   "WHERE datetime >= '" + DateFrom + " 00:00:00' AND datetime <= '" + DateTo + " 00:00:00'" \
                   "ORDER BY datetime ASC"
        self.StockData = pd.read_sql(SqlQuery, Connection, index_col='datetime')

    def SetTimeFrame(self, TimeFrame):
        Conversion = {'open': 'first', 'high': 'max', 'low': 'min', 'close': 'last', 'vol': 'sum'}
        InTimeFrame = self.StockData.resample(TimeFrame, how=Conversion)
        return InTimeFrame[(InTimeFrame.vol >= 0)]

    def SMA(self, Period, TimeFrame, PriceType, Shift={ 'quantity': 0, 'freq': 'Min'}):
        InTimeFrame = self.SetTimeFrame(TimeFrame)
        InTimeFrameShift = InTimeFrame.shift(Shift['quantity'], freq=Shift['freq'])
        return pd.rolling_mean(InTimeFrameShift, Period)[[PriceType]].rename(columns={PriceType: "SMA_"+PriceType+"_"+str(Period)+"_"+TimeFrame})