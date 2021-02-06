from flask import Flask,redirect,url_for,render_template,jsonify,request
import pymongo
import re
import urllib.parse

from time_tools import sum_duration

import sys

sys.path.append('.') # Adds higher directory to python modules path.
from scrap_playlist import recup_bdd_headless,recup_info


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

client = pymongo.MongoClient('mongodb',27017)
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
			data=data,
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
			channel=data)
	else:

		return('404')


@app.route('/livescraper/')
def livescraper():

	return render_template('livescraper.html')

@app.route('/livescraper/<playlist_id>')
def livescraper_search(playlist_id):

	data = { 'id':playlist_id}

	for i in range(100000000):
		pass


	return jsonify(data)
	

@app.route('/api/s/<word>')
def api_search(word):
	"""
	API Search View 

	View used to retrieve results from user input in the search bar

	Args:

		word: user search input 
		
	Returns:
		
		json_data: data for search bar results as json (REST Api)

	"""
	
	word = urllib.parse.unquote(word) 
	
	#Regex to avoid injection or mistakes
	if re.match(r'[^a-zA-Z\s]+',word) is not None:
		return(jsonify([]))


	quotation = lambda w: re.sub(r'(\w+)','"\g<1>"',w)

	word = ' '.join(list(map(quotation,word.split())))

	collection = database['playlist']
	
	data = list(collection.find({'$text':{'$search':word}}).limit(15))

	for el in data:
		el['playlist_duration'] = sum_duration(el['video_time'])
	json_data = jsonify(data)

	return(json_data)

@app.route('/api/p/<channel_id>')
def api_get_playlist(channel_id):
	"""
	API Get Playlist View 

	View used to retrieve playlist from channel_id

	Args:

		channel_id: youtube id of the channel
		
	Returns:
		
		json_data: playlist data linked with the channel às json (REST Api)

	"""
	collection = database['playlist']

	data = list(collection.find({'id_youtubeur': channel_id}))

	json_data = jsonify(data)

	return(json_data)


if __name__ == "__main__":
	app.run(host="0.0.0.0",debug=True)
