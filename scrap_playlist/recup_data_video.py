import selenium
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from pymongo import MongoClient

def recup_info(lien):
    CHROME_PATH = "./chromedriver"

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome = webdriver.Chrome(executable_path=CHROME_PATH,
                              options=chrome_options
                             )
    chrome.get(lien)
    time.sleep(1)
    tag = chrome.find_elements_by_id('info')

    if tag[0].text[0] == '#':
        res = tag[0].text.split('\n')[2].split('vues')[0]
        vues = res.replace('\u202f','')
        vues = vues.replace('vues', '')
        vues = int(vues)
        res2 = tag[0].text
        res2 = res2.split('\n')
        titre = res2[1]
        like = res2[3]
        dislike = res2[4]

    else :
        res = tag[0].text.split('\n')[1].split('vues')[0]
        vues = res.replace('\u202f','')
        vues = vues.replace('vues', '')
        vues = int(vues)
        res2 = tag[0].text
        res2 = res2.split('\n')
        titre = res2[0]
        like = res2[2]
        dislike = res2[3]

    question = re.findall(r'[,]',like)
    if len(question)!=0:
        like = like.replace('K', '00')
        like = like.replace('M', '00000')
        like = like.replace('Md', '00000000')
        like = like.replace(',','')
        like = like.replace(' ', '')
        like = int(like)
    else :
        like = like.replace('K', '000')
        like = like.replace('M', '000000')
        like = like.replace('Md', '000000000')
        like = like.replace(' ', '')
        like = int(like)

    question2 = re.findall(r'[,]',dislike)
    if len(question2)!=0:
        dislike = dislike.replace('K', '00')
        dislike = dislike.replace('M', '00000')
        dislike = dislike.replace('Md', '00000000')
        dislike = dislike.replace(',','')
        dislike = dislike.replace(' ', '')
        dislike = int(dislike)

    else :
        dislike = dislike.replace('K', '000')
        dislike = dislike.replace('M', '000000')
        dislike = dislike.replace('Md', '000000000')
        dislike = dislike.replace(' ', '')
        dislike = int(dislike)
    bdd = ({'titre' : titre,
                    'likes' : like,
                    'dislikes' : dislike,
                    'vues' : vues
                   })
    return bdd

if '__name__' == '__main__':
    pass
