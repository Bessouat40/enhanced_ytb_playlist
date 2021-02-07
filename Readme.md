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

