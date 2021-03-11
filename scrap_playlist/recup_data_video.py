import selenium
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
import pymongo
from pymongo import MongoClient
import datetime


def recup_info(lien):

    url = f"https://www.youtube.com/watch?v={lien}"

    """CHROME_PATH = "./chromedriver"
                
                    chrome_options = Options()
                    chrome_options.add_argument("--headless")
                    chrome = webdriver.Chrome(executable_path=CHROME_PATH,
                                              options=chrome_options
                                             )"""

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1080,720")
    # chrome_options.add_argument('--disable-dev-shm-usage')

    chrome = webdriver.Remote("http://selenium:4444/wd/hub", options=chrome_options)

    chrome.get(url)
    time.sleep(2.5)

    tag = chrome.find_elements_by_id("info")

    info = tag[0].text.split("\n")

    f = open("log.txt", "a")
    f.write(url + "\n" + str(info) + "\n")
    f.close()

    if len(info) == 1:
        chrome.quit()
        return None

    if "Private video" in info:
        chrome.quit()
        return None

    info.remove("SHARE")
    info.remove("SAVE")

    if "Unlisted" in info:
        info.remove("Unlisted")

    dislike = info[-1]
    like = info[-2]
    titre = info[-4]

    vues = list(filter(None, [t.text for t in chrome.find_elements_by_id("count")]))[0]
    vues = vues.replace("\u202f", "").replace("views", "").replace(",", "")
    vues = int(vues)

    post_date = chrome.find_element_by_id("date").text

    post_date = re.sub("•", "", post_date)
    post_date = re.sub("Premiered\s", "", post_date)
    post_date = re.sub("Streamed live on\s", "", post_date)

    if "," in post_date:
        post_date = datetime.datetime.strptime(post_date, "%b %d, %Y")
    else:
        post_date = datetime.datetime.strptime(post_date, "%b %d %Y")

    question = re.findall(r"[,]", like)
    if len(question) != 0:
        like = like.replace("K", "00")
        like = like.replace("M", "00000")
        like = like.replace("Md", "00000000")
        like = like.replace(".", "")
        like = like.replace(" ", "")
        like = int(like)
    else:
        like = like.replace("K", "000")
        like = like.replace("M", "000000")
        like = like.replace("Md", "000000000")
        like = like.replace(".", "")
        like = like.replace(" ", "")
        like = int(like)

    question2 = re.findall(r"[,]", dislike)
    if len(question2) != 0:
        dislike = dislike.replace("K", "00")
        dislike = dislike.replace("M", "00000")
        dislike = dislike.replace("Md", "00000000")
        dislike = dislike.replace(".", "")
        dislike = dislike.replace(" ", "")
        dislike = int(dislike)

    else:
        dislike = dislike.replace("K", "000")
        dislike = dislike.replace("M", "000000")
        dislike = dislike.replace("Md", "000000000")
        dislike = dislike.replace(".", "")
        dislike = dislike.replace(" ", "")
        dislike = int(dislike)

    # duration = chrome.find_elements_by_class_name('ytp-time-duration')[0].text
    # Not working because of ads

    bdd = {
        "titre": titre,
        "likes": like,
        "dislikes": dislike,
        "vues": vues,
        "post_date": post_date,
    }

    print(bdd)

    chrome.quit()

    return bdd


if __name__ == "__main__":

    client = pymongo.MongoClient("mongodb", 27017)
    db = client["youtube"]
    collection = db["videos"]
    video_list = list(collection.find({"titre": {"$exists": False}}))

    for v in video_list:
        print(v)

        data = recup_info(v["_id"])

        if data is not None:
            collection.update_one({"_id": v["_id"]}, {"$set": data})
        else:
            print("cant be accessed")
