class Event(object):
    pass


class MarketEvent(Event):

    def __init__(self):
        self.type = 'MARKET'


class SignalEvent():

    #Обрабатывает событие отправки Signal из объекта Strategy. Его получает объект Portfolio, который предпринимает нужное действие.


    def __init__(self, symbol, datetime, signal_type):

        #Инициализирует SignalEvent.

        #symbol - Символ тикера, например для Google — 'GOOG'.
        #datetime - временная метка момента генерации сигнала.
        #signal_type - 'LONG' или 'SHORT' '''

        self.type = 'SIGNAL'
        self.symbol = symbol
        self.datetime = datetime
        self.signal_type = signal_type