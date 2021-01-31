from ytb_api import YoutubeAPI
import pymongo
import os

API_KEY = os.environ['API_KEY']

ytb = YoutubeAPI(API_KEY)
client = pymongo.MongoClient('mongodb',27017)

database = client[ytb.db]
collection = database['videos']

data = list(collection.find({}))

for item in data:

	comments = ytb.get_video_comments(item['_id'])
	ytb.to_mongo(comments,'comments')

