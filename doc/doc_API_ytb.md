## ytb-api

Il s'agit ici d'un wrapper partiel de l'API [Youtube Data  API v3](https://developers.google.com/youtube/v3/docs).

L'API nous est utile pour récupérer les identifiants des chaînes en lien avec la programmation ainsi que des commentaires présents sous les vidéos

> :warning: Il est nécessaire d'obtenir une clé API pour l'utiliser.

Ce wrappeur peut être utilisé en ligne de commande :

```bash
 python ytb_api.py -h
 
 usage: ytb_api.py [-h] [-a A] [-l L] [-c C] [-t T]

Youtube API Wrapper

optional arguments:
  -h, --help           show this help message and exit
  -a A, -api_key A     Youtube API Key
  -l L, -list L        Name of the .txt file that contains the list of keyword
                       to use in search
  -c C, -collection C  Mongo Collection to use for insert
  -t T, -type T        Type of the ressource to search
```

Ou bien comme une librarie Python :

```Python
from ytb_api import YoutubeAPI
import os

API_KEY = os.environ['API_KEY']
FILE = 'mylist.txt'
RESSOURCE = 'channels'



ytb = YoutubeAPI(API_KEY)
data = ytb.search_from_file(FILE,RESSOURCE)
print(data)

```
