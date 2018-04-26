from binance.client import Client


class Binance:

    __client = None

    def __init__(self):
        self.__client = Client('', '', {"verify": True, "timeout": 30})

    def ping_server(self):
        return ('Down', 'Up')[len(self.__client.ping()) == 0]

    def get_pair_info(self, pair):
        return self.__client.get_symbol_info(str(pair))

    def get_pair_status(self, pair):
        return self.get_pair_info(pair)['status']

    def get_historical_klines(self, symbol, interval, start_str, end_str=None):
        return self.__client.get_historical_klines(symbol, interval, start_str, end_str)

