from django.core.management.base import BaseCommand
from myapps.crypto.notify.telegram_bot import _send_message as sm


class Command(BaseCommand):

    help = 'Send telegram message'

    def handle(self, *args, **options):
        try:
            # Get new data for Binance market
            sm.run()
        except Exception as ex:
            self.stdout.write('Send message process has not been completed, there is an error: {0}'.format(ex))