### Machine Learning

Pour classifier les commentaires  positif et négatif, et ainsi obtenir un score représentatif des avis nous nous sommes basée sur un algorithme de type régression logistique, permettant ainsi une classification binaire (bien que l'analyse de sentiment ne s'arrête pas à Positif/Négatif)

Les étapes de développement ont été les suivantes:
  - Récupération des commentaires via le wrapper de  l'API Youtube
  - Classification manuelle en positif/négatif à l'aide du module Python [trunklocator](https://github.com/Dumbris/trunklucator)
  - Pre-processing et entrainement sur le notebook Jupyter
  - Choix des paramètres
  - Sauvegarde du modèle et du vectorizer puis mise en production
