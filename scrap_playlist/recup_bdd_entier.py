#!pip install pymongo
from pymongo import MongoClient #création de notre collection qui va contenir les infos

#pour l'exemple on initialise une liste de noms de youtubeurs qui va simuler ce qu'on utilisera plus tard
liste_ytbeurs = {'id' : ['UCWeg2Pkate69NFdBeuRFTAw','UCI0vQvr9aFn27yR6Ej6n5UA','UCIlUBOXnXjxdjmL_atU53kA','UCMV8ybQXuvInI5lYw2Wzfjw'] ,
                 'chaine' : ['squeezie','Real Python', 'Cours Python 3','Python 3 Dersleri']}

#pour que la fonction s'exécute sans erreur, il faut que le fichier chromedriver soit dans le même répertoire que ce fichier python
def recup_bdd_headless(id_chaine) :
    """
    Fonction qui prend en entrée le nom de la chaîne youtube
    """ Fonction qui prend en entrée le nom de la chaîne youtube
    dont ou souhaite récupérer les informations

    Arg:
        chaine: string correspondant au nom de la chaîne youtube

    Returns:
        dictionnaire comportant plusieurs informations sur la chaîne youtube"""

    arg chaine : string correspondant au nom de la chaîne youtube
    return : dictionnaire comportant plusieurs informations sur la chaîne youtube"""
    IS_LINUX = False

    CHROME_PATH = "./chromedriver"

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome = webdriver.Chrome(executable_path=CHROME_PATH,
                              options=chrome_options
                              chrome_options=chrome_options
                             )

    #récupération des données
    #récuparation des données
    bdd = []
    lien = 'https://www.youtube.com/channel/{}/playlists?view=1&sort=dd&shelf_id=0'.format(id_chaine)
    chrome.get(lien)
@@ -50,97 +49,42 @@ def recup_bdd_headless(id_chaine) :
    l_title = list(filter(None,l_title))

    for idx,i in enumerate(l_url) :

            last_modif = ''
            print('url:',i)
        try :
            chrome.get(i)
            tag = chrome.find_element_by_id("stats")
            res = []
            for j in tag.find_elements_by_tag_name('span'):
                res.append(j.text)

            #Obtenir image
            img = chrome.find_elements_by_css_selector('img')[0].get_attribute('src')

            desc = chrome.find_element_by_id('description')

            desc_tag = desc.find_elements_by_tag_name('yt-formatted-string')

            video_time = chrome.find_elements_by_class_name('style-scope ytd-thumbnail-overlay-time-status-renderer')
            video_time = list(filter(None,[v.text for v in video_time]))

            if len(desc_tag)>0:
                description = desc_tag[0].text
            else:
                description = ''
            nbr_videos = res[0]
            try :
                last_modif = res[2]+res[3]+res[4]
                last_modif = last_modif.replace('Mise à jour il y a','')

            if len(res)>0:
                nbr_videos = res[0]
                if len(res)==5:
                    last_modif = res[2]+res[3]+res[4]
                    last_modif = last_modif.replace('Mise à jour il y a','')
            except :
                last_modif = res[2]+res[3]
                last_modif = last_modif.replace('Dernière modification le','')

                if len(res)==4:
                    last_modif = res[2]+res[3]
                    last_modif = last_modif.replace('Dernière modification le','')

                if len(res)==2:
                    nbr_videos = 0
                    last_modif = res[1]
            else:
                #Si une video la liste est vide
                nbr_videos = 1
                last_modif = ''

            vues = chrome.find_element_by_xpath("//yt-formatted-string[2]").text
            vues = vues.replace('\u202f','')



            id_playlist = re.findall(r'https:\/\/www\.youtube\.com\/playlist\?list=([a-zA-Z0-9-_]*)',i)[0]

            bdd.append({ '_id' : id_playlist,
                    'id_youtubeur' : id_chaine,
            bdd.append({'id_youtubeur' : id_chaine,
                    'playlist' : l_title[idx],
                    'nbr_videos' : nbr_videos,
                    'derniere_maj' : last_modif,
                    'vues' : vues,
                    'url_img' : img,
                    'description': description,
                    'video_time': video_time,
                    'derniere_MAJ' : last_modif,
                    'vues' : vues
                   })

        except : None
    chrome.quit()
    return bdd

#ici on commence à créer la bdd Mongo
client = MongoClient()
db_test = client['youtube']

db = client['youtube']
collection = db['channels']
ytb_list = list(collection.find({}))

liste_ytbeurs = [v['_id'] for v in ytb_list]

col_playlist = db['playlist']
data=[]

#liste_ytbeurs = ['UCq6XkhO5SZ66N04IcPbqNcw']
col_youtubeur = db_test['id_youtubeur']
for i in range(len(liste_ytbeurs)):

    print(i,'/',len(liste_ytbeurs))
    print(liste_ytbeurs[i])

    if len(list(col_playlist.find({ 'id_youtubeur': liste_ytbeurs[i]})))==0:

        data = recup_bdd_headless(liste_ytbeurs[i])

        if data:
            try:
                col_playlist.insert_many(data)
                print('Inserted')
            except:
                import sys
                print(" \n Unexpected error: \n", sys.exc_info()[0])

col_playlist.create_index( [("$**", "text")])
    col_youtubeur.insert_one({'id' : liste_ytbeurs['id'][i], 'chaine' : liste_ytbeurs['chaine'][i]})
col_playlist = db_test['playlist']
data=[]
for i in range(len(liste_ytbeurs['id'])):
    data = recup_bdd_headless(liste_ytbeurs['id'][i])
    col_playlist.insert_many(data)
