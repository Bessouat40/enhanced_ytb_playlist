import requests
import json
import sys
import argparse
import re
from datetime import datetime

import pymongo
from pymongo.errors import BulkWriteError


class YoutubeAPI:
    """
    Python Wrapper of Youtube Data API v3

    Based on Python Requests module


    Youtube Data API v3
    https://developers.google.com/youtube/v3/docs

    """

    def __init__(self, api_key):
        """
        Initializing

        """

        self.api_key = api_key
        self.client = pymongo.MongoClient("mongo")
        self.db = self.client["youtube"]

    def search_channels(self, keyword, nb_res="50", lang="en"):
        """

        Searching for channels

            Args:

                keyword: keyword to search channel

                nb_res: number of results (50 max)

            Return:

                channel_info: list of json channel object
        """

        keyword = re.sub(" ", "%s", keyword)

        # Formatting the url with parameters
        url = "https://youtube.googleapis.com/youtube/v3/search?type=channel&part=snippet&maxResults={n_res}&q={kw}&key={api_key}&relevanceLanguage={lang}"
        url_formatted = url.format(
            n_res=nb_res, kw=keyword, api_key=self.api_key, lang=lang
        )

        # Sending the GET request to Youtube API
        req = requests.get(url_formatted)
        print(req.text)
        json_result = json.loads(req.text)["items"]

        # Extracting Data from json response
        channel_info = [
            {
                "channel_title": v["snippet"]["channelTitle"],
                "_id": v["snippet"]["channelId"],
                "channel_description": v["snippet"]["description"],
                "img": v["snippet"]["thumbnails"]["default"]["url"],
                "created": datetime.strptime(
                    v["snippet"]["publishTime"], "%Y-%m-%dT%H:%M:%SZ"
                ),
                "last_update": datetime.now(),
            }
            for v in json_result
        ]

        return channel_info

    def search_from_file(self, file, search_type="channels"):
        """

        Searching for channels using a list of keyword
            contained in a .txt file

            Args:

                file: name of the file that contains the keywords

                search_type: only channels at the time

            Return:

                results: list of list json object
        """

        print(f"Reading from {file} ...")

        results = []
        try:
            with open(file) as f:
                for line in f:
                    results.append(self.search_channels(line))

            return results
        except FileNotFoundError:
            print(".txt file not found")
            sys.exit(0)

    def get_video_comments(self, video_id, nb_res="100"):
        """

        Getting comments from a video, based on Id


            Args:

                video_id: id of the video

                nb_res: number of comments to get, in the 1-100 range

            Return:

                results: list of list json object
        """

        base_str = "https://youtube.googleapis.com/youtube/v3/commentThreads?part=snippet&maxResults={nb_res}&order=time&videoId={video_id}&key={api_key}"

        url_formatted = base_str.format(
            nb_res=nb_res, video_id=video_id, api_key=self.api_key
        )

        req = requests.get(url_formatted)

        try:
            json_result = json.loads(req.text)["items"]
            comments = [
                {
                    "_id": v["id"],
                    "video_id": v["snippet"]["videoId"],
                    "author_name": v["snippet"]["topLevelComment"]["snippet"][
                        "authorDisplayName"
                    ],
                    "text": v["snippet"]["topLevelComment"]["snippet"]["textOriginal"],
                    "author_profile_picture": v["snippet"]["topLevelComment"][
                        "snippet"
                    ]["authorProfileImageUrl"],
                    "author_id": v["snippet"]["topLevelComment"]["snippet"][
                        "authorChannelId"
                    ]["value"],
                    "likes": v["snippet"]["topLevelComment"]["snippet"]["likeCount"],
                    "date_published": datetime.strptime(
                        v["snippet"]["topLevelComment"]["snippet"]["publishedAt"],
                        "%Y-%m-%dT%H:%M:%SZ",
                    ),
                    "date_updated": datetime.strptime(
                        v["snippet"]["topLevelComment"]["snippet"]["updatedAt"],
                        "%Y-%m-%dT%H:%M:%SZ",
                    ),
                    "replies": v["snippet"]["totalReplyCount"],
                }
                for v in json_result
            ]
        except KeyError:
            comments = None

        return comments

    def to_mongo(self, data, mongo_collection):
        """

        Send Data to the Mongo DB registred in config.json

        Create text index to retrieve data

            Args:

                data: json data to be inserted in the mongo db

                mongo_collection: name of the collection

        """

        collection = self.db[mongo_collection]

        for l in data:
            try:
                if l:
                    collection.insert_many(l)

            # Error log
            except BulkWriteError as error:
                err = error.details
                print("*********************")
                print(err["writeErrors"][0]["errmsg"])
                print("Inserted : ", err["nInserted"])
                print("Upserted : ", err["nUpserted"])
                print("Modified : ", err["nModified"])
                print("Removed : ", err["nRemoved"])
                print("*********************")

        # Create Index
        collection.create_index([("$**", "text")])  # Crée / Vérifie index text


if __name__ == "__main__":

    # CLI Interface

    parser = argparse.ArgumentParser(description="Youtube API Wrapper")
    parser.add_argument("-a", "-api_key", help="Youtube API Key", type=str)
    parser.add_argument(
        "-l",
        "-list",
        help="Name of the .txt file that contains the list of keyword to use in search",
        type=str,
    )
    parser.add_argument(
        "-c", "-collection", help="Mongo Collection to use for insert", type=str
    )
    parser.add_argument(
        "-t",
        "-type",
        default="channels",
        help="Type of the ressource to search",
        type=str,
    )
    args = parser.parse_args()

    if args.a:
        api_key = args.a
    else:
        try:
            api_key = os.environ["API_KEY"]
        except:
            print("Youtube Api key missing")
            sys.exit(0)

    if args.l:
        file = args.l
    else:
        print("file missing")
        sys.exit(0)

    if args.c:
        collection = args.c
    else:
        print("collection missing")
        sys.exit(0)

    if args.t:
        ressource_type = args.t

    ytb = YoutubeAPI(api_key)
    data = ytb.search_from_file(file, ressource_type)
    ytb.to_mongo(data, collection)
