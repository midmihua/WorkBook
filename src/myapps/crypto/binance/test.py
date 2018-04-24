from binance.client import Client


cl = Client('', '', {"verify": True, "timeout": 20})


if __name__ == "__main__":

    print(cl.ping())
    print(cl.get_server_time())
    print(cl.get_system_status())
    # print(cl.get_exchange_info()) # Huge data returned
    # print(cl.get_symbol_info('BNBBTC'))
    # print(cl.get_order_book(symbol='STORJBTC'))
    # print(cl.get_recent_trades(symbol='STORJBTC'))
    # print(cl.get_aggregate_trades(symbol='STORJBTC'))
    # print(cl.get_klines(symbol='STORJBTC', interval=Client.KLINE_INTERVAL_30MINUTE))

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

    # fetch 1 minute klines for the last day up until now
    # klines = client.get_historical_klines("BNBBTC", Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")
    print(cl.get_historical_klines("STORJBTC", Client.KLINE_INTERVAL_1MINUTE, "1 hour ago UTC"))

    # fetch 30 minute klines for the last month of 2017
    # klines = client.get_historical_klines("ETHBTC", Client.KLINE_INTERVAL_30MINUTE, "1 Dec, 2017", "1 Jan, 2018")

    # fetch weekly klines since it listed
    # klines = client.get_historical_klines("NEOBTC", KLINE_INTERVAL_1WEEK, "1 Jan, 2017")
