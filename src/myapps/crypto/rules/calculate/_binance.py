from myapps.crypto.models import RuleMap
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

    rule_map = RuleMap.objects.filter(status=STATUS_ACTIVE)

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


def run():

    # Rule: pump_dump
    print('1. pump_dump calculation is started')
    calc_pump_dump()
    print('2. pump_dump calculation is finished')