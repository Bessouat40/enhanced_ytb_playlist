from ytb_api import YoutubeAPI
import pymongo

ytb = YoutubeAPI()
client = pymongo.MongoClient(ytb.mongo_url,ytb.mongo_port)

database = client[ytb.mongo_db]
collection = database['videos']

data = list(collection.find({}))

for item in data:

	comments = ytb.get_video_comments(item['_id'],100)
	ytb.to_mongo(comments,'comments')

