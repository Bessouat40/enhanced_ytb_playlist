#importation des bibliothèques nécessaires
import selenium
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#importation bibliothèque bdd Mongo
#!pip install pymongo
from pymongo import MongoClient #création de notre collection qui va contenir les infos

import time


def recup_bdd_headless(id_chaine) :
    """ 
    Fonction qui prend en entrée le nom de la chaîne youtube
    dont ou souhaite récupérer les informations
    
    Arg: 
        chaine: string correspondant au nom de la chaîne youtube
    
    Returns: 
        dictionnaire comportant plusieurs informations sur la chaîne youtube"""
    

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=640,10500")
    #chrome_options.add_argument('--disable-dev-shm-usage')       

    driver = webdriver.Remote('http://selenium:4444/wd/hub',options=chrome_options)
    
    #récupération des données
    bdd = []
    lien = 'https://www.youtube.com/channel/{}/playlists?view=1&sort=dd&shelf_id=0'.format(id_chaine)
    driver.get(lien)
    driver.refresh()
    tag = driver.find_elements_by_css_selector('a')
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
        
            last_modif = ''
            print('url:',i)
            driver.get(i)
            
            tag = driver.find_element_by_id("stats")
            res = [j.text for j in tag.find_elements_by_tag_name('span')]

            #Obtenir image
            img = driver.find_elements_by_css_selector('img')[0].get_attribute('src')

            desc = driver.find_element_by_id('description')

            desc_tag = desc.find_elements_by_tag_name('yt-formatted-string')
            

            video_time = driver.find_elements_by_class_name('style-scope ytd-thumbnail-overlay-time-status-renderer')
           
            #print([v.text for v in video_time])
            
            video_time = list(filter(None,[v.text for v in video_time]))

    
            video_links = driver.find_elements_by_css_selector('a')

            video_ids = []

            for l in video_links:
                lien = str(l.get_attribute('href'))
               
                if re.match(r'https://www\.youtube\.com/watch\?v=(\S+)&list=\S+&index=\d+',lien):

                    video_ids.append(re.findall(r'https://www\.youtube\.com/watch\?v=(\S+)&list=\S+',lien)[0])

            video_ids = set(video_ids)

            if len(desc_tag)>0:
                description = desc_tag[0].text
            else:
                description = ''

            if len(res)>0:
                nbr_videos = res[0]
                if len(res)==5:
                    last_modif = res[2]+res[3]+res[4]
                    last_modif = last_modif.replace('Mise à jour il y a','')
                    last_modif = re.sub(r'Updated','',last_modif)
                    last_modif = re.sub(r'(\d{1,2})(\w*)',last_modif)

                if len(res)==4:
                    last_modif = res[2]+res[3]
                    last_modif = last_modif.replace('Dernière modification le','')
                    last_modif = re.sub('Last updated on','',last_modif)
                
                if len(res)==2:
                    nbr_videos = 1
                    last_modif = res[1]
            else:
                #Si une video la liste est vide
                nbr_videos = 1
                last_modif = ''
                
            vues = driver.find_element_by_xpath("//yt-formatted-string[2]").text
            vues = vues.replace('\u202f','')
            vues = vues.replace('views','')
            vues = vues.replace(',','')
            


            id_playlist = re.findall(r'https:\/\/www\.youtube\.com\/playlist\?list=([a-zA-Z0-9-_]*)',i)[0]

            bdd.append({ '_id' : id_playlist,
                    'id_youtubeur' : id_chaine,
                    'playlist' : l_title[idx],
                    'nbr_videos' : nbr_videos,
                    'derniere_maj' : last_modif,
                    'vues' : vues,
                    'url_img' : img,
                    'description': description,
                    'video_time': video_time,
                   })
        
    driver.quit()
    return bdd

if '__name__' == '__main__':
    #ici on commence à créer la bdd Mongo
    client = MongoClient('mongodb',27017)

    db = client['youtube']
    collection = db['channels']
    ytb_list = list(collection.find({}))

    liste_ytbeurs = [v['_id'] for v in ytb_list]

    col_playlist = db['playlist']
    data=[]

    #liste_ytbeurs = ['UCeVMnSShP_Iviwkknt83cww'] # Test Value
    for i in range(len(liste_ytbeurs)):

        print(i,'/',len(liste_ytbeurs))
        print(liste_ytbeurs[i])

        if len(list(col_playlist.find({ 'id_youtubeur': liste_ytbeurs[i]})))==0:
            
            data = recup_bdd_headless(liste_ytbeurs[i])

            if data:
                try:
                    col_playlist.insert_many(data)
                    col_playlist.create_index( [("$**", "text")])         
                    print('Inserted')
                except:
                    import sys
                    print(" \n Unexpected error: \n", sys.exc_info()[0])

