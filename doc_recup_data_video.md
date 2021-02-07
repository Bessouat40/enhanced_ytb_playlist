# Documentation de la fonction recup_data_video

## Fonctionnement
Recup_data_video permet de récupérer des informations à propos d'une vidéo youtube.
A l'aide du lien d'une vidéo, la fonction va permettre d'obtenir le titre, le nombre de vues, le nombre de likes et de dislikes.

## Paramètres de la fonction

La fonction a **1 paramètres** :
- lien : ce paramètre correspond au lien de la vidéo que l'on veut scrapper. C'est un paramètre de type string.

## Variables importantes de la fonction

- chrome : variable qui permet de naviguer sur google chrome et ainsi accéder aux éléments html qui nous intéressent,
- tag : variable qui contient la partie de la page web qui nous intéresse. Contient les informations concernant la vidéo dont on souhaite récupérer les informations,
- question/question2 : variables qui permettent de savoir si il y a une virgule dans le nombre de likes et de dislikes. En effet, si il y a une virgule ou pas, nous n'effectuerons pas les mêmes actions.

## Return de la fonction

La fonction renvoie un dictionnaire **bdd**.  
Il associe à chaque mot : 'titre', 'like', 'dislike', 'vues' sa valeur.
Utiliser un dictionnaire permet d'accéder facilement aux informations qu'on recherche. Ainsi on obtient une base de données structurée et facilement utilisable.