from flask import Flask,redirect,url_for,render_template,jsonify,request
import pymongo
import re

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
	return render_template("playlist.html")

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


@app.route('/api/<word>')
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

	collection = database['channels']
	
	data = list(collection.find( { '$text' : { '$search': word } }).limit(7))
	json_data = jsonify(data)

	return(json_data)
	
if __name__ == "__main__":
	app.run(debug=True)
