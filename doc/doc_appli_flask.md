## Flask WebApp

Il s'agit ici d'une application web Flask écrite en Python.

Elle comporte deux types de fonctions :
 - Les views classiques qui permettent de renvoyer un template de page et des données
 - Les views type REST API qui renvoient des données au format JSON afin de pouvoir permettre des interactions avec les pages et d'obtenir d'autres données
 
 
 ### Views classiques 
 
  - home : renvoit le template de la page d'accueil
  - playlist_page : renvoit le template de la page d'une playlist avec les données associées à la playlist dont l'identifiant est passé dans l'url
  - channel_page : renvoit le template de la page d'une chaîne avec les données associées à la chaîne dont l'identifiant est passé dans l'url
  - livescraper :  renvoit le template de la page du livescraper
  
  ### Views API
  
  - livrescraper_search : renvoit les données issus du scrapping de la playlist dont l'ID est passé en paramètre. Dans un premier temps, on scrap la page de la playlist pour récupérer des informations (vues,nombre de vidéos, durées, id des vidéos), puis les pages des vidéos pour récupérer les informations type like, dislike, vues. Les données récoltés sont ensuite misent en forme au format json et triée chronologiquement.
  
  - api_search : renvoit les données pour la fonction de recherche de playlist, les mots clés sont isolés  et nettoyés avant de faire une requête dans la base de données Mongo et de renvoyer le résultat avec un pre-processing pour calculer la durée totale (qui aurait aussi pu être réalisé en javascript)
  
  - api_get_playlist : renvoit les données des playlists associées à une chaine, à travers une requête Mongo.
  
  
