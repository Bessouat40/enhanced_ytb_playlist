## Récupération des Playlists 

### recup_playlist_from_channels

Cette fonction permet de récupérer les url et titres des playlists d'une chaine à partir de l'id de cette dernière.

Arguments: 
  
  - string correspondant au nom de la chaîne youtube
    
Returns: 
  
- liste des titres des playlists, liste de leurs urls
 
 ### get_playlist_data
 
 Cette fonction permet de récupérer les informations d'une playlist à partir de son url ou id
 
Arguments:
 
- string correspond à l'url de la playlist
- (facultatif) id de la chaine si on souhaite sauvegarder cette information
- id de la playlist si on ne posséde pas l'url
   
Returns:
 
- dictionnaire contenant les informations de la playlist
- dictionnaire content les id des vidéos de la playlist
