from django.core.management.base import BaseCommand
from myapps.tryinsta.update import api


class Command(BaseCommand):

    help = 'Upload new data from Instagram'

    def handle(self, *args, **options):
        try:
            # Get new data for Instagram
            api.get_data()
        except Exception as ex:
            self.stdout.write('Refresh process has not been completed, there is an error: {0}'.format(ex))