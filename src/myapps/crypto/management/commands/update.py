from django.core.management.base import BaseCommand
from myapps.crypto.refresh.binan import _refresh as binance_refresh


class Command(BaseCommand):

    help = 'Upload new data from remote market to local database'

    def handle(self, *args, **options):
        try:
            # Get new data for Binance market
            binance_refresh.run()
        except Exception as ex:
            self.stdout.write('Refresh process has not been completed, there is an error: {0}'.format(ex))