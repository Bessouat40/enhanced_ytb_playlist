import requests
import json
import sys, getopt
from datetime import datetime

import pymongo
from pymongo.errors import BulkWriteError


help_string = 'ytb.py -l <keywordfile>'

class YoutubeAPI:
    
    def __init__(self):
        
        try:
            f = open('config.json','r') 
            data = json.load(f) 
            f.close() 
        
        except FileNotFoundError:
            print('config.json not found')
            sys.exit(0)
        
        self.api_key = data['api-key']
        self.mongo_url = data['db']['mongo-url']
        self.mongo_port = data['db']['mongo-port']
        self.mongo_db = data['db']['mongo-db-name']
        self.mongo_collection = data['db']['mongo-collection-name']
            
    def search_channels(self,keyword,nb_res="50"):
        
        if ' ' in keyword:
            keyword.replace(' ','%s')
            
        url = "https://youtube.googleapis.com/youtube/v3/search?type=channel&part=snippet&maxResults={n_res}&q={kw}&key={api_key}"
        url_formatted = url.format(n_res=nb_res,kw=keyword,api_key=self.api_key)
        req = requests.get(url_formatted)
        json_result = json.loads(req.text)['items']
        channel_info = [{"channel_title":v['snippet']['channelTitle'],
                         "_id": v['snippet']['channelId'],
                         "channel_description": v['snippet']['description'],
                         "img": v['snippet']['thumbnails']['default']['url'],
                         "created": datetime.strptime(v['snippet']['publishTime'], '%Y-%m-%dT%H:%M:%SZ'),
                         "last_update":datetime.now()}  for v in json_result]
    
        return(channel_info)
    
    def search_from_file(self,file,search_type="channels"):

        print(f'Reading from {file}...')
        results = []
        try:
            with open(file) as f:
                for line in f:
                    results.append(self.search_channels(line))

            return(results)
        except FileNotFoundError:
            print('.txt file not found')
            sys.exit(0)
            
    
    def to_mongo(self,data):
        
        client = pymongo.MongoClient(self.mongo_url,self.mongo_port)
        database = client[self.mongo_db]
        collection = database[self.mongo_collection]
        
        for l in data:
            try:
                collection.insert_many(l)
                
            except BulkWriteError as error:
                z = error.details
                print("*********************")
                print(z['writeErrors'][0]['errmsg'])
                print("Inserted : ",z['nInserted'])
                print("Upserted : ",z['nUpserted'])
                print("Modified : ",z['nModified'])
                print("Removed : ",z['nRemoved'])
                print("*********************")    


        #collection.create_index([('channel_title','text'),('channel_description', 'text')])
        collection.create_index( [("$**", "text")])

if __name__ == "__main__":

    
    argv = sys.argv[1:]

    try:
        opts, args = getopt.getopt(argv,"hl:")
    except getopt.GetoptError:
       print(help_string)
       sys.exit(0)

    for opt, arg in opts:

        if opt == '-h':
            print(help_string)
            sys.exit(0)

        elif opt == '-l':
            ytb = YoutubeAPI()
            results = ytb.search_from_file(arg)
            ytb.to_mongo(results) 

        