from django.core.management.base import BaseCommand
from myapps.crypto.rules.calculate import _binance as binance_calculate


class Command(BaseCommand):

    help = 'Calculate rules mapped to Binance market'

    def handle(self, *args, **options):
        try:
            # Get new rules results
            binance_calculate.run()
        except Exception as ex:
            self.stdout.write('Calculate process has not been completed, there is an error: {0}'.format(ex))