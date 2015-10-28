class Event(object):
    pass


class MarketEvent(Event):

    def __init__(self):
        self.type = 'MARKET'


class SignalEvent(Event):

    def __init__(self, symbol, datetime, signal_type):

        #Инициализирует SignalEvent.

        #symbol - Символ тикера, например для Google — 'GOOG'.
        #datetime - временная метка момента генерации сигнала.
        #signal_type - 'LONG' или 'SHORT' '''

        self.type = 'SIGNAL'
        self.symbol = symbol
        self.datetime = datetime
        self.signal_type = signal_type


class OrderEvent(Event):

    def __init__(self, symbol, order_type, quantity, direction):

        #symbol - Инструмент, сделку с которым нужно осуществить.
        #order_type - 'MKT' или 'LMT' для приказов Market или Limit.
        #quantity - определения количества единиц инструмента.
        #direction - 'BUY', 'SELL', 'STOP_LOSS' и 'TAKE_PROFIT'

        self.type = 'ORDER'
        self.symbol = symbol
        self.order_type = order_type
        self.quantity = quantity
        self.direction = direction


class FillEvent(Event):

    def __init__(self, timeindex, symbol, exchange, quantity, direction, fill_cost, commission=None):
        #timeindex - Разрешение баров в момент выполнения ордера.
        #symbol - Инструмент, по которому прошла сделка.
        #exchange - Биржа, на которой была осуществлена сделка.
        #quantity - Количество единиц инструмента в сделке.
        #direction - Направление исполнения ('BUY' или 'SELL')
        #ill_cost - Размер обеспечения.
        #commission - Опциональная комиссия, информация отправляемая бркоером.

        self.type = 'FILL'
        self.timeindex = timeindex
        self.symbol = symbol
        self.exchange = exchange
        self.quantity = quantity
        self.direction = direction
        self.fill_cost = fill_cost
        self.commission = commission