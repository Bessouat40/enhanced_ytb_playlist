#Obtaining the channels 
python ./ytb-api/get_channels.py
#Obtaining the playlist linked to these channels
python ./scrap_playlist/recup_bdd.py
#Obtaining the videos linked to these playlist
python ./scrap_playlist/recup_data_video.py