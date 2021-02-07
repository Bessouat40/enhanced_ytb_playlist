## ytb-api

Il s'agit ici d'un wrapper partiel de l'API [Youtube Data  API v3](https://developers.google.com/youtube/v3/docs).

L'API nous est utile pour récupérer les identifiants des chaînes en lien avec la programmation ainsi que des commentaires présents sous les vidéos

Ce wrappeur peut être utilisé en ligne de commande :
```
 python ytb_api.py -h
```

Ou bien comme une librarie Python :

```Python
from ytb_api import YoutubeAPI
import os

API_KEY = os.environ['API_KEY']
FILE = 'mylist.txt'
RESSOURCE = 'channels'
COLLECTION = 'channels'


ytb = YoutubeAPI(API_KEY)
data = ytb.search_from_file(FILE,RESSOURCE)
print(data)

```
