from flask import Flask,redirect,url_for,render_template,jsonify

import pymongo

app = Flask(__name__)

app.secret_key = "M10kUCghakjlZVhvba5sFaw"
app.config['JSON_AS_ASCII'] = False

client = pymongo.MongoClient('localhost',27017)
        

@app.route('/')
def home():
	return render_template("index.html")

@app.route('/p/<playlist_id>')
def playlist_page(playlist_id):
	pass
	return render_template("playlist.html")

@app.route('/c/<channel_id>')
def channel_page(channel_id):
	database = client['projet']
	collection = database['channels']

	data = list(collection.find({"_id":channel_id}))[0]
	

	return render_template("channel.html",
		channel_id=data['_id'],
		channel_title=data['channel_title'],
		channel_description=data['channel_description'],
		channel_img=data['img'])

@app.route('/api/<word>')
def api_search(word):
	
	database = client['projet']
	collection = database['channels']
	
	data = list(collection.find( { '$text' : { '$search': word } }).limit(7))
	
	return(jsonify(data))
	
if __name__ == "__main__":
	app.run(debug=True)
