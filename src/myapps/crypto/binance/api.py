from binance.client import Client


class Binance:

    __client = None
    __pair = None

    def __init__(self, pair):
        self.__client = Client('', '', {"verify": True, "timeout": 20})
        self.__pair = pair

    def get_historical_klines(self, interval, start_date, end_date = None):
        return self.__client.get_historical_trades(self.__pair, interval, start_date, end_date)
