from instagram.client import InstagramAPI


access_token = ""
client_secret = ""
client_id = ""

'''
api = InstagramAPI(access_token=access_token, client_secret=client_secret)
recent_media = api.user_recent_media()
for media in recent_media:
    print(media)
'''

api = InstagramAPI(client_id=client_id, client_secret=client_secret)
popular_media = api.media_popular(count=20)
for media in popular_media:
    print(media.images['standard_resolution'].url)