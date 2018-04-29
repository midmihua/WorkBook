from binance.client import Client


class Binance:

    __client = None

    def __init__(self):
        self.__client = Client('', '', {"verify": True, "timeout": 30})

    def ping_server(self):
        return ('Down', 'Up')[len(self.__client.ping()) == 0]

    def get_system_status(self):
        return self.__client.get_system_status()

    def get_pair_info(self, pair):
        return self.__client.get_symbol_info(str(pair))

    def get_market_depth(self, pair):
        return self.__client.get_order_book(symbol=pair)

    def get_recent_trades(self, pair):
        return self.__client.get_recent_trades(symbol=pair)

    def get_24h_ticker(self, pair):
        return self.__client.get_ticker(symbol=pair)

    def get_historical_candlesticks(self, symbol, interval, start_str, end_str=None):
        return self.__client.get_historical_klines(symbol, interval, start_str, end_str)

