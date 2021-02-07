# Youtube Playlist Enhanced

![screenshot](https://github.com/Bessouat40/enhanced_ytb_playlist/blob/main/doc/readme_img.PNG?raw=true)

## Introduction

Nous nous sommes rendus compte que souvent, lorsqu'on veut apprendre un nouveau langage de programmation, notre premier réflexe est d'aller voir sur youtube les différents tutoriels proposés.
Mais il y a un problème qui se pose... Bien souvent, il existe beaucoup de youtubeurs qui proposent ce type de contenu. On peut donc très vite être submergé d'informations et ne pas savoir quelle playlist choisir.

## Solution proposée

C'est pourquoi nous avons imaginé une application web : **Youtube Playlist Enhanced**, qui permettra aux personnes de présenter les différents tutoriels présents sur la plateforme de manière à mieux diriger leurs choix.
Notre présentation se fera selon plusieurs critères qui sont susceptibles d'être pertinents aux yeux de l'utilisateur, et dont certains ne sont pas proposé par Youtube. 

Les critères que nous avons choisi de retenir sont :
- le nombre de vues de chaque playlist
- le nombre de like et de dislikes de la playlist
- la durée totale de la playlist
- l'évolution du nombre de vues au cours des vidéos de la playlist.

Nous proposons aussi une analyse des commentaires les plus pertinents de certaines vidéos de la playlist afin que l'utilisateur se fasse une idée de l'avis des personnes qui ont regardé le contenu avant lui.

## Bonus Livescraper

Notre application permettra aussi à l'utilisateur de récupérer des informations sur la playlist qu'il aura séléctionner, en copiant l'url de cette dernière dans l'outil de scraping.

## Possibilités d'améliorations
 
Dans le futur, nous pourrions élargir notre base de données pré-existante à l'aide de contenus qui diffèrent de tutoriels de programmation. 
Par exemple nous pourrions imaginer d'autres catégories telles que la cuisine, des programmes sportifs, ...

## Technologies Utilisées

 - Front-End : Bootstrap, ChartJS & Vanilla JS
 - Back-End : Flask (Python)
 - Scraping : Selenium (Python)
 - Base de Données : MongoDB
 - DevOps : Docker 
 - Versioning : Git
 - Machine Learning : Scikit Learn (Python)

## Installation avec Docker

Tout d'abord il faut cloner le repo

``` 
git clone https://github.com/Bessouat40/enhanced_ytb_playlist.git 
```
Puis construire les images 

```
docker-compose build
docker-compose -up -d
```

## Documentation

Nous avons mis à votre disposition la documentation concernant les fonctions que nous utilisons dans notre programme.
Il y a 4 principales fonctions :

- [ytb-api](https://github.com/Bessouat40/enhanced_ytb_playlist/tree/main/doc/doc_API_ytb.md)
- [Flask Webapp](https://github.com/Bessouat40/enhanced_ytb_playlist/tree/main/doc/doc_appli_flask.md)
- [recup_bdd](https://github.com/Bessouat40/enhanced_ytb_playlist/tree/main/doc/doc_recup_bdd.md)
- [recup_data_video](https://github.com/Bessouat40/enhanced_ytb_playlist/tree/main/doc/doc_recup_data_video.md)

## Comment remplir la BDD si besoin
> :warning: Il est nécessaire d'obtenir une clé d'API Youtube .
> :warning: Avec une clé gratuite le nombre de requête à l'API Youtube est limité .
> :warning: Le scraper de playlist prend beaucoup de temps à s'éxecuter et peut prendre jusqu'a 2GO de RAM et 100% du CPU.
 
 - Avant de construire l'image Docker, obtenir une clef d'API Youtube auprès de Google et la placer entre les quotes de la variable d'environnement dans le Dockerfile
 - Construire et le conteneur
 - Ouvrir l'invite de commandes du conteneur webapp
 - Taper ``` bash ``` pour accèder au prompt bash
 - Entrer cd ytb-api puis si besoin modifier les mots clés à utiliser pour la recherche en éditant le fichier mylist.txt
 - Lancer la recherche et remplir la DB de chaîne utiliser l'outil en ligne de commande (cf doc) ou lancer le script get_channels.py avec 'python get_channels.py'
 - Revenir en arrière avec  cd .. 
 - Aller dans le dossier du scraper avec cd scrap_playlist 
 - Lancer le scraper de playlist pour remplir la collection playlist de la DB : python recup_bdd.py 
 - Puis lancer le scraper de vidéo pour remplir la collection vidéo de la DB : python recup_data_video.py
