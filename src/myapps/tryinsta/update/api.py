# from instagram.client import InstagramAPI
# from myapps.tryinsta._conf import ACCESS_TOKEN, CLIENT_SECRET, CLIENT_ID

import requests
from myapps.tryinsta.models import TCUser, TCUserMedia

# api = InstagramAPI(access_token=ACCESS_TOKEN, client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
# print(api.user('7745256822').counts)
# print(api.user_recent_media(user_id='7745256822'))
# print(api.tag_recent_media(tag_name='midmihtest'))


def get_data():

    # Get data
    cookies = dict(sessionid='IGSCbca0bbfa9e7c69dbc16411ef118572766c931a6b806dfedfe267d76785595a7b%3AoglrhbtesB9Gh7jeIYIH91YW14vDPkdV%3A%7B%22_auth_user_id%22%3A7745256822%2C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiveModelBackend%22%2C%22_auth_user_hash%22%3A%22%22%2C%22_platform%22%3A4%2C%22_token_ver%22%3A2%2C%22_token%22%3A%227745256822%3AwPJCMxVrU7j5KlFBrxeVmUF3V8fZ7sk5%3A5fb358d97086b9b61ce3b9006761577863614ed6d321411947b3f309115ac349%22%2C%22last_refreshed%22%3A1526423675.2318284512%7D')
    r = requests.get("https://api.instagram.com/v1/tags/midmihtest/media/recent.json?access_token=7745256822.d27f795.33cc0e1122864b06bc183bab4695214f&sig=9d78a06178be2b95ca565cc31c9509536d8a75c98b279805604fa17ad80d2039&sig=9d78a06178be2b95ca565cc31c9509536d8a75c98b279805604fa17ad80d2039",
                     cookies=cookies)

    # Insert into db
    print(r.status_code)
    print(r.url)

    # Get all TC users
    users = TCUser.objects.all()

    if len(users) > 0:

        for user in users:

            for i in r.json()['data']:

                obj, created = TCUserMedia.objects.update_or_create(
                    username=user,
                    media_id=i['id'],
                    defaults={
                        'media_tags': i['tags'],
                        'media': i['images']
                    }
                )
