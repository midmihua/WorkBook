import time

from myapps.crypto.markets.binan.api import Binance
from myapps.crypto.models import Market, Stat

# Constants
BINANCE_MARKET = 'binance'
STATUS_ACTIVE = 'AC'
SLEEP_TIME = 1


# Instance to communicate with Binance API
client = Binance()


def pair_info(pair):
    return client.get_pair_info(pair)


def market_depth(pair):
    return client.get_market_depth(pair)


def recent_trades(pair):
    return client.get_recent_trades(pair)


def _24h_ticker(pair):
    return client.get_24h_ticker(pair)


def historical_candlesticks(pair, interval, start_str, end_str=None):
    return client.get_historical_candlesticks(pair, interval, start_str, end_str)


def market_status():

    market = Market.objects.filter(market=BINANCE_MARKET).filter(status=STATUS_ACTIVE)

    if market:
        remote_data = client.get_system_status()
        obj, created = Market.objects.update_or_create(
            pk=market,
            defaults={
                'market_status': remote_data
            }
        )
    else:
        print('{0} market is not found in configuration or has inactive status'.format(BINANCE_MARKET))


def get_stat():

    pairs = Stat.objects.filter(status=STATUS_ACTIVE)

    if len(pairs) > 0:
        for pair in pairs:
            obj, created = Stat.objects.update_or_create(
                pk=pair.pk,
                defaults={
                    'pair_info': pair_info(pair.pair.get_name()),
                    'market_depth': market_depth(pair.pair.get_name()),
                    'recent_trades': recent_trades(pair.pair.get_name()),
                    '_24h_ticker': _24h_ticker(pair.pair.get_name()),
                    'historical_candlesticks':
                        historical_candlesticks(
                            pair.pair.get_name(),
                            pair.get_interval(),
                            pair.get_period()
                        )
                }
            )
            # Stop process for 1 sec to avoid host blocking
            time.sleep(SLEEP_TIME)
    else:
        print('Active pairs have not been found for {0} market'.format(BINANCE_MARKET))


def run():
    print('1. Data refresh process is started')

    print('2. market_status() refresh is started')
    market_status()
    print('3. market_status() refresh is finished')

    print('4. get_stat() refresh is started')
    get_stat()
    print('5. get_stat() refresh is finished')

    print('6. Data refresh process is finished')
