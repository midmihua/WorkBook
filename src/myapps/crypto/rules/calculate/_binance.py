from myapps.crypto.models import RuleMap, Rule
from myapps.crypto.rules.list import pump_dump


# Constants
STATUS_ACTIVE = 'AC'


""" Object to serialize
[
    [
        1499040000000,      # Open time
        "0.01634790",       # Open
        "0.80000000",       # High
        "0.01575800",       # Low
        "0.01577100",       # Close
        "148976.11427815",  # Volume
        1499644799999,      # Close time
        "2434.19055334",    # Quote asset volume
        308,                # Number of trades
        "1756.87402397",    # Taker buy base asset volume
        "28.46694368",      # Taker buy quote asset volume
        "17928899.62484339" # Can be ignored
    ]
]
"""


def calc_pump_dump():

    rule = Rule.objects.filter(rule='pump_dump')
    rule_map = RuleMap.objects.filter(rule=rule).filter(status=STATUS_ACTIVE)

    if len(rule_map) > 0:

        for pair_rule in rule_map:

            start = pair_rule.stat.historical_candlesticks[0]
            end = pair_rule.stat.historical_candlesticks[-1]

            calc_result = {
                "start": {
                    "open_time": start[0],
                    "open_price": start[1],
                    "high_price": start[2],
                    "low_price": start[3],
                    "close_price": start[4],
                    "volume": start[5],
                    "close_time": start[6],
                    "quote_asset_volume": start[7],
                    "number_of_trades": start[8]
                },
                "end": {
                    "open_time": end[0],
                    "open_price": end[1],
                    "high_price": end[2],
                    "low_price": end[3],
                    "close_price": end[4],
                    "volume": end[5],
                    "close_time": end[6],
                    "quote_asset_volume": end[7],
                    "number_of_trades": end[8]
                },
                "res": pump_dump.get_results(float(start[1]), float(end[4]))
            }

            # Add results to database
            obj, created = RuleMap.objects.update_or_create(
                pk=pair_rule.id,
                defaults={
                    'result': calc_result
                }
            )


""" Object to serialize
{
    'openTime': 1526827080031,
    'symbol': 'BNBBTC',
    'lowPrice': '0.00160670',
    'prevClosePrice': '0.00166280',
    'lastQty': '0.03000000',
    'priceChange': '-0.00001040',
    'count': 77744,
    'priceChangePercent': '-0.625',
    'closeTime': 1526913480031,
    'askQty': '29.76000000',
    'openPrice': '0.00166470',
    'weightedAvgPrice': '0.00165774',
    'bidQty': '12.10000000',
    'lastId': 19172650,
    'bidPrice': '0.00165200',
    'firstId': 19094907,
    'highPrice': '0.00172000',
    'quoteVolume': '5387.58009698',
    'askPrice': '0.00165430',
    'lastPrice': '0.00165430',
    'volume': '3249960.11000000'
}
"""


def calc_price_change_percent():

    rule = Rule.objects.filter(rule='price_change_percent')
    rule_map = RuleMap.objects.filter(rule=rule).filter(status=STATUS_ACTIVE)

    if len(rule_map) > 0:

        for pair_rule in rule_map:

            # Add results to database
            obj, created = RuleMap.objects.update_or_create(
                pk=pair_rule.id,
                defaults={
                    'result': pair_rule.stat._24h_ticker
                }
            )


def run():

    # Rule: pump_dump
    print('1. pump_dump calculation is started')
    calc_pump_dump()
    print('2. pump_dump calculation is finished')

    print('3. price_change_percent calculation is started')
    calc_price_change_percent()
    print('4. price_change_percent calculation is finished')