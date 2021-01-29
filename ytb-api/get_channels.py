from ytb_api import YoutubeAPI

API_KEY = ##########
FILE = 'mylist.txt'
RESSOURCE = 'channels'
COLLECTION = 'channels'


ytb = YoutubeAPI(API_KEY)
data = ytb.search_from_file(FILE,RESSOURCE)
ytb.to_mongo(data,COLLECTION)