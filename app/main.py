from flask import Flask,redirect,url_for,render_template,jsonify,request
import pymongo
import re

from time_tools import sum_duration

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

client = pymongo.MongoClient('localhost',27017)
database = client['youtube']
        
@app.route('/')
def home():
	"""
	Home View

	Returns:

		index.html: HTML Template for home page
	
	"""
	return render_template("index.html")

@app.route('/p/<playlist_id>')
def playlist_page(playlist_id):
	"""
	Playlist View

	Args: 

		playlist_id: Youtube id of the playlist, used to look in the db 
	
		"""
	collection = database['playlist']

	data = collection.find_one({"_id":playlist_id})
	
	if data:

		return render_template("playlist.html",
			playlist_id=data['_id'],
			playlist_title=data['playlist'],
			playlist_description=data['description'],
			playlist_img=data['url_img'],
			channel_id=data['id_youtubeur'],
			playlist_views=data['vues'],
			playlist_nb_videos=data['nbr_videos'],
			playlist_last_update=data['derniere_maj'],
			playlist_duration=sum_duration(data['video_time']))

	else:
		return('404')

@app.route('/c/<channel_id>')
def channel_page(channel_id):
	"""
	Channel View

	Find channel info to create channel page

	Args:

		channel_id: Youtube id of the channel, used to look in the db

	Returns:

		channel.html: HTML Template for channel page

		channel_id: Youtube id of the channel

		channel_title: Name of the channel

		channel_description : Description of the channel

	"""
	collection = database['channels']

	data = collection.find_one({"_id":channel_id})
	
	if data:

		return render_template("channel.html",
			channel_id=data['_id'],
			channel_title=data['channel_title'],
			channel_description=data['channel_description'],
			channel_img=data['img'])
	else:

		return('404')


@app.route('/api/s/<word>')
def api_search(word):
	"""
	API Search View 

	View used to retrieve results from user input in the search bar

	Args:

		word: user search input 
		
	Returns:
		
		json_data: data for search bar results as json (rest api)

	"""
	#Regex to avoid injection or mistakes
	word = re.sub(r"\W","",word) 

	collection = database['playlist']
	
	data = list(collection.find( { '$text' : { '$search': word } }).limit(10))

	for el in data:
		el['playlist_duration'] = sum_duration(el['video_time'])
	json_data = jsonify(data)

	return(json_data)
	
if __name__ == "__main__":
	app.run(debug=True)
