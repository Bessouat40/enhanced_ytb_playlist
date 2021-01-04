#importation des bibliothèques nécessaires
import selenium
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#importation bibliothèque bdd Mongo
#!pip install pymongo
from pymongo import MongoClient #création de notre collection qui va contenir les infos

#pour l'exemple on initialise une liste de noms de youtubeurs qui va simuler ce qu'on utilisera plus tard
liste_ytbeurs = {'id' : ['UCWeg2Pkate69NFdBeuRFTAw','UCI0vQvr9aFn27yR6Ej6n5UA','UCIlUBOXnXjxdjmL_atU53kA','UCMV8ybQXuvInI5lYw2Wzfjw'] ,
                 'chaine' : ['squeezie','Real Python', 'Cours Python 3','Python 3 Dersleri']}

#pour que la fonction s'exécute sans erreur, il faut que le fichier chromedriver soit dans le même répertoire que ce fichier python
def recup_bdd_headless(id_chaine) :
    """ Fonction qui prend en entrée le nom de la chaîne youtube
    dont ou souhaite récupérer les informations
    arg chaine : string correspondant au nom de la chaîne youtube
    return : dictionnaire comportant plusieurs informations sur la chaîne youtube"""
 

    CHROME_PATH = "./chromedriver"

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome = webdriver.Chrome(executable_path=CHROME_PATH,
                              chrome_options=chrome_options
                             )

    #récuparation des données
    bdd = []
    lien = 'https://www.youtube.com/channel/{}/playlists?view=1&sort=dd&shelf_id=0'.format(id_chaine)
    chrome.get(lien)
    chrome.refresh()
    tag = chrome.find_elements_by_css_selector('a')
    l_url = []
    l_title = []
    for a in tag:
        url = a.get_attribute('href')
        try:
            if url.startswith("https://www.youtube.com/playlist?"):
                l_url.append(url)
            if url.startswith("https://www.youtube.com/watch?"):
                l_title.append(a.get_attribute('title'))
        except:
            pass

    l_title = list(filter(None,l_title))

    for idx,i in enumerate(l_url) :
        try :
            chrome.get(i)
            tag = chrome.find_element_by_id("stats")
            res = []
            for j in tag.find_elements_by_tag_name('span'):
                res.append(j.text)
            nbr_videos = res[0]
            try :
                last_modif = res[2]+res[3]+res[4]
                last_modif = last_modif.replace('Mise à jour il y a','')

            except :
                last_modif = res[2]+res[3]
                last_modif = last_modif.replace('Dernière modification le','')

            vues = chrome.find_element_by_xpath("//yt-formatted-string[2]").text
            vues = vues.replace('\u202f','')
           
            print(l_url[idx])
            playlist_id=re.findall(r"list=(\w+)",l_url[idx])[0]
            print(playlist_id)
            
            bdd.append({'_id': playlist_id,
                    'playlist' : l_title[idx],
                    'nbr_videos' : nbr_videos,
                    'derniere_MAJ' : last_modif,
                    'vues' : vues
                   })
        except : None
    chrome.quit()
    return bdd

#ici on commence à créer la bdd Mongo
client = MongoClient()
db_test = client['youtubeurs']

for i in range(len(liste_ytbeurs['id'])):
    globals()['collection'+str(i)] = db_test[liste_ytbeurs['chaine'][i]]
    data = recup_bdd_headless(liste_ytbeurs['id'][i])
    globals()['collection'+str(i)].insert_many(data)

print(db_test.collection_names())
