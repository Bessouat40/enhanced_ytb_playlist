# Enhanced playlist

## Introduction

Nous nous sommes rendus compte que souvent, lorsqu'on veut apprendre un nouveau langage de programmation, notre premier réflexe est d'aller voir sur youtube les différents tutoriels proposés.
Mais il y a un problème qui se pose... Bien souvent, il existe beaucoup de youtubeurs qui proposent ce type de contenu. On peut donc très vite être submergé d'informations et ne pas savoir quelle playlist choisir.

## Solution proposée

C'est pourquoi nous avons imaginé une application web : **Enhanced youtube playlist**, qui permettra aux personnes de présenter les différents tutoriels présents sur la plateforme de manière à mieux diriger leurs choix.
Notre présentation se fera selon plusieurs critères qui sont susceptibles d'être pertinents aux yeux de l'utilisateur. 

Les critères que nous avons choisi de retenir sont :
- le nombre de vues de chaque playlist,
- le nombre de like et de dislikes de la playlist,
- la durée de la playlist,
- l'évolution du nombre de vues au cours des vidéos de la playlist.

Nous proposons aussi une analyse des commentaires les plus pertinents de certaines vidéos de la playlist afin que l'utilisateur se fasse une idée de l'avis des personnes qui ont regardé le contenu avant lui.

## Bonus apporté par notre application

Notre application permettra aussi à l'utilisateur de récupérer des informations en temps réel sur une vidéo qu'il aura lui-même sélectionné.

## Possibilités d'améliorations

Dans le futur, nous pourrions élargir notre base de données pré-existante à l'aide de contenus qui diffèrent de tutoriels de programmation. 
Par exemple nous pourrions imaginer d'autres catégories telles que la cuisine, des programmes sportifs, ...

## Requirements

Afin de bien faire fonctionner notre programme, vous devez avoir installé :
- Docker,
- Python

En ce qui concerne les librairies python, vous devez avoir installé les librairies :
- flask,
- pymongo,
- re,
- urllib.parse,
- time_tools,
- time,
- selenium,
- sys,
- requests,
- json,
- argparse,
- datetime,
- os,

## Documentation

Nous avons mis à votre disposition la documentation concernant les fonctions que nous utilisons dans notre programme.
Il y a 4 principales fonctions :
- [recup_bdd](https://github.com/Bessouat40/enhanced_ytb_playlist/tree/main/doc/doc_recup_bdd.md),
- [API-YTB](https://github.com/Bessouat40/enhanced_ytb_playlist/tree/main/doc/doc_API_ytb.md),
- [appli_flask](https://github.com/Bessouat40/enhanced_ytb_playlist/tree/main/doc/doc_appli_flask.md),
- [recup_data_video](https://github.com/Bessouat40/enhanced_ytb_playlist/tree/main/doc/doc_recup_data_video.md)

