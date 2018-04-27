from myapps.crypto.markets.binan import Binance
from myapps.crypto.markets.graph import *


cl = Binance('STORJBTC')


if __name__ == "__main__":

    """
    [
        [
            1499040000000,  # Open time
            "0.01634790",  # Open
            "0.80000000",  # High
            "0.01575800",  # Low
            "0.01577100",  # Close
            "148976.11427815",  # Volume
            1499644799999,  # Close time
            "2434.19055334",  # Quote asset volume
            308,  # Number of trades
            "1756.87402397",  # Taker buy base asset volume
            "28.46694368",  # Taker buy quote asset volume
            "17928899.62484339"  # Can be ignored
        ]
    ]
    """

    """
    KLINE_INTERVAL_1MINUTE = '1m'
    KLINE_INTERVAL_3MINUTE = '3m'
    KLINE_INTERVAL_5MINUTE = '5m'
    KLINE_INTERVAL_15MINUTE = '15m'
    KLINE_INTERVAL_30MINUTE = '30m'
    KLINE_INTERVAL_1HOUR = '1h'
    KLINE_INTERVAL_2HOUR = '2h'
    KLINE_INTERVAL_4HOUR = '4h'
    KLINE_INTERVAL_6HOUR = '6h'
    KLINE_INTERVAL_8HOUR = '8h'
    KLINE_INTERVAL_12HOUR = '12h'
    KLINE_INTERVAL_1DAY = '1d'
    KLINE_INTERVAL_3DAY = '3d'
    KLINE_INTERVAL_1WEEK = '1w'
    KLINE_INTERVAL_1MONTH = '1M'
    """

    # fetch 1 minute klines for the last day up until now
    # klines = client.get_historical_klines("BNBBTC", Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")
    # print(cl.get_historical_klines("STORJBTC", Client.KLINE_INTERVAL_1MINUTE, "1 hour ago UTC"))

    # fetch 30 minute klines for the last month of 2017
    # klines = client.get_historical_klines("ETHBTC", Client.KLINE_INTERVAL_30MINUTE, "1 Dec, 2017", "1 Jan, 2018")

    # fetch weekly klines since it listed
    # klines = client.get_historical_klines("NEOBTC", KLINE_INTERVAL_1WEEK, "1 Jan, 2017")

    # data = cl.get_historical_klines('30m', '4 hour ago UTC')
    # show_graph(data)

    # for line in data:
    #     print(line)
