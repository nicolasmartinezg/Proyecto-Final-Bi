import requests
import pandas as pd
import json
import boto3
from botocore.client import Config
import os
#credenciales para acceder a la api de Deezer
DEEZER_APP_ID = "446902"
DEEZER_APP_SECRET = "154639e6aa1f2214186f80adbe2d5b3b"
DEEZER_REDIRECT_URI = "http://developers.deezer.com/api"



# POST
auth_response = requests.post(DEEZER_REDIRECT_URI, {
    'grant_type': 'client_credentials',
    'client_id': DEEZER_APP_ID,
    'client_secret': DEEZER_APP_SECRET,
})







#EndPoints de el usuario 1-------------------------------------------------------------------------------------------------------------------
#base url para consultar las canciones favoritas del usuario 1
BASE_URL_CANCIONES_FAVORITAS = 'https://api.deezer.com/user/2605858862/tracks?limit=901'
#base url para consultar los artistas favoritos del usuario 1
BASE_URL_ARTISTAS_FAVORITOS = 'https://api.deezer.com/user/2605858862/artists?limit=89'
cf=requests.get(BASE_URL_CANCIONES_FAVORITAS)
favoritas=cf.json()
with open('canciones favoritas usuario1.json', 'w') as f:
    json.dump(favoritas, f, indent=4, sort_keys=True)

af=requests.get(BASE_URL_ARTISTAS_FAVORITOS)
Afavoritos=af.json()
with open('Artistas favoritos usuario1.json', 'w') as f:
    json.dump(Afavoritos, f, indent=4, sort_keys=True)

# base url consultar las canciones de el playlist1 del usuario 1
BASE_URL_Tracks = 'https://api.deezer.com/playlist/5982817864/tracks?limit=699'
cancionesPlaylist=requests.get(BASE_URL_Tracks)
cp=cancionesPlaylist.json()
with open('PlayList1 usuario1.json', 'w') as f:
    json.dump(cp, f, indent=4, sort_keys=True)
# base url consultar las canciones de el playlist2 del usuario 1
BASE_URL_Tracks2 = 'https://api.deezer.com/playlist/7472023284/tracks?limit=168'
cancionesPlaylist2=requests.get(BASE_URL_Tracks2)
cp2=cancionesPlaylist2.json()
with open('PlayList2 usuario1.json', 'w') as f:
    json.dump(cp2, f, indent=4, sort_keys=True)
# base url consultar las canciones de el playlist3 del usuario 1
BASE_URL_Tracks3 = 'https://api.deezer.com/playlist/971831493/tracks?limit=475'
cancionesPlaylist3=requests.get(BASE_URL_Tracks2)
cp3=cancionesPlaylist3.json()
with open('PlayList3 usuario1.json', 'w') as f:
    json.dump(cp3, f, indent=4, sort_keys=True)
#--------------------------------------------------------------------------------------------------------------------------------------------

#Endpoints Artista Jbalvin

# base URL of all Deezer API endpoints
#base url que me muestra todos los playlist del artista J Balvin
BASE_URL = 'https://api.deezer.com/artist/4860761/playlists?limit=100'
#base url que me muestra todos los seguidores de J Balvin
BASE_URL_Seguidores = 'https://api.deezer.com/artist/4860761/fans?limit=100'
#base url que me muestra todos los album de Jbalvin
BASE_URL_Album = 'https://api.deezer.com/artist/4860761/albums?limit=100'
BASE_URL_Canciones = 'https://api.deezer.com/search?q=j balvin&limit=290'
# convertir los datos traidos de la url de los playlist del Artista en formato json
response= requests.get(BASE_URL)
r = response.json()
#convertir los datos traidos de la url de los fans del artista en formato json
datos= requests.get(BASE_URL_Seguidores)
fans = datos.json()
#convertir los datos traidos de la url de los album del artista en formato json
datos1= requests.get(BASE_URL_Album)
album= datos1.json()
#convertir los datos traidos de la url de las canciones del artista en formato json
datos2= requests.get(BASE_URL_Canciones)
canciones= datos2.json()

# guardar el json de los playlist de jbalvin como archivo
with open('PlayList JBalvin.json', 'w') as f:
    json.dump(r, f, indent=4, sort_keys=True)


# guardar el json de los fans de jbalvin como archivo
with open('fans J Balvin.json', 'w') as f:
    json.dump(fans, f, indent=4, sort_keys=True)

#guardar album
with open('Album J Balvin.json', 'w') as f:
    json.dump(album, f, indent=4, sort_keys=True)
#guardar cansiones de jBalvin
with open('canciones J Balvin.json', 'w') as f:
    json.dump(canciones, f, indent=4, sort_keys=True)


#EndPoints del Usuario 2 ----------------------------------------------------------------------------------------------------------------------------

#Url para consultar las canciones favoritas del usuario 2--------------------------------------------------------------------------------------------
URL_CANCIONES_FAVORITAS = "https://api.deezer.com/user/4039239222/tracks?limit=1656"
lc = requests.get(URL_CANCIONES_FAVORITAS)
jFavoritas = lc.json()
#Guardar canciones del usuario 2
with open('canciones favoritas usuario 2.json', 'w') as e:
    json.dump(jFavoritas, e, indent=4, sort_keys=True)

#Url para consultar los artistas favoritos del usuario 2-----------------------------------------------------------------------------------------------
URL_ARTISTAS_FAVORITOS2 = "https://api.deezer.com/user/4039239222/artists?limit=41"
la = requests.get(URL_ARTISTAS_FAVORITOS2)
jArtistas = la.json()
#Guardar Artistas favoritos del usuario 2
with open('artistas favoritos usuario 2.json', 'w') as e:
    json.dump(jArtistas, e, indent=4, sort_keys=True)

#consultar las PlayList del usuario 2---------------------------------------------------------------------------------------------------------

#Url Playlist 1
URL_PLAYLIST_1 = "https://api.deezer.com/playlist/8416193362/tracks?limit=50"
lr1 = requests.get(URL_PLAYLIST_1)
jPlayList1 = lr1.json()
#Guardar PlayList 1 del usuario 2
with open('playlist 1  usuario 2.json', 'w') as e:
    json.dump(jPlayList1, e, indent=4, sort_keys=True)
#Url PlayList 2
URL_PLAYLIST_2 = "https://api.deezer.com/playlist/1098908237/tracks?limit=50"
lr2 = requests.get(URL_PLAYLIST_2)
jPlayList2 = lr2.json()
#Guardar PlayList 2 del usuario 2
with open('playlist 2  usuario 2.json', 'w') as e:
    json.dump(jPlayList2, e, indent=4, sort_keys=True)

#Url PlayList 3
URL_PLAYLIST_3 = "https://api.deezer.com/playlist/8311123682/tracks?limit=50"
lr3 = requests.get(URL_PLAYLIST_3)
jPlayList3 = lr3.json()
#Guardar PlayList 3 del usuario 2
with open('playlist 3  usuario 2.json', 'w') as e:
    json.dump(jPlayList3, e, indent=4, sort_keys=True)

#Url PlayList 4
URL_PLAYLIST_4 = "https://api.deezer.com/playlist/3114195306/tracks?limit=50"
lr4 = requests.get(URL_PLAYLIST_4)
jPlayList4 = lr4.json()
#Guardar PlayList 4 del usuario 2
with open('playlist 4  usuario 2.json', 'w') as e:
    json.dump(jPlayList4, e, indent=4, sort_keys=True)

#Url PlayList 5
URL_PLAYLIST_5 = "https://api.deezer.com/playlist/6750169864/tracks?limit=50"
lr5 = requests.get(URL_PLAYLIST_5)
jPlayList5 = lr5.json()
#Guardar PlayList 5 del usuario 2
with open('playlist 5  usuario 2.json', 'w') as e:
    json.dump(jPlayList5, e, indent=4, sort_keys=True)

#credenciales para establecer la conexion con AWS
ACCESS_KEY_ID =  "AKIASCCE5URAFIEVDIQA"
ACCESS_SECRET_KEY = "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"
BUCKET_NAME = 'pruebasproyectofinal'




client = boto3.client(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version='s3v4')
)
#cargar info del usuario 1---------------------------------------------------------------------------------------------------------------------
#guardar info de las canciones favoritas del usuario 1 en s3
upload_file_key = 'Usuarios/'+'1Usuario/'+'Canciones Favoritas/' + 'canciones favoritas usuario1.json'
client.upload_file('canciones favoritas usuario1.json', BUCKET_NAME, upload_file_key)
#guardar info de los artistas favoritos del usuario 1 en s3
upload_file_key = 'Usuarios/'+'1Usuario/'+'Artistas Favoritos/' + 'Artistas favoritos usuario1.json'
client.upload_file('Artistas favoritos usuario1.json', BUCKET_NAME, upload_file_key)
#guardar info de las canciones del playlist1 del usuario 1 en s3
upload_file_key = 'Usuarios/'+'1Usuario/'+'PlayLists/' +'PlayList1 usuario1.json'
client.upload_file('PlayList1 usuario1.json', BUCKET_NAME, upload_file_key)
#guardar info de las canciones del playlist2 del usuario 1 en s3
upload_file_key = 'Usuarios/'+'1Usuario/'+'PlayLists/' +'PlayList2 usuario1.json'
client.upload_file('PlayList2 usuario1.json', BUCKET_NAME, upload_file_key)
#guardar info de las canciones del playlist3 del usuario 1 en s3
upload_file_key = 'Usuarios/'+'1Usuario/'+'PlayLists/' +'PlayList3 usuario1.json'
client.upload_file('PlayList3 usuario1.json', BUCKET_NAME, upload_file_key)
#------------------------------------------------------------------------------------------------------------------------------------------------------
#cargar info de el Artista Jbalvin
#guardar todos los  playlist del artista J Balvin en s3
upload_file_key = 'Artistas/'+'JBalvin/'+'PlayList/' + 'PlayList JBalvin.json'
client.upload_file('PlayList JBalvin.json', BUCKET_NAME, upload_file_key)
#guardar todos los fans del artista JBalvin en s3
upload_file_key = 'Artistas/'+'JBalvin/'+'Fans/' + 'fans J Balvin.json'
client.upload_file('fans J Balvin.json', BUCKET_NAME, upload_file_key)
#guardar todos los album del artista Jbalvin en s3
upload_file_key = 'Artistas/'+'JBalvin/'+'Albums/' + 'Album J Balvin.json'
client.upload_file('Album J Balvin.json', BUCKET_NAME, upload_file_key)
#guardar todas las canciones de jBalvin
upload_file_key = 'Artistas/'+'JBalvin/'+'canciones/' + 'canciones J Balvin.json'
client.upload_file('canciones J Balvin.json', BUCKET_NAME, upload_file_key)
#------------------------------------------------------------------------------------------------------------------------------------------------------

#Guardar información del usuario 2 en S3
upload_file_key = 'Usuarios/'+'2Usuario/'+'Canciones Favoritas/' + 'canciones favoritas usuario 2.json'
client.upload_file('canciones favoritas usuario 2.json', BUCKET_NAME, upload_file_key)


#Guardar informacion de los Artistas favoritos del Usuario 2 en S3
upload_file_key = 'Usuarios/'+'2Usuario/'+'Artistas Favoritos/' + 'artistas favoritos usuario 2.json'
client.upload_file('artistas favoritos usuario 2.json', BUCKET_NAME, upload_file_key)
#Guardar PlayList 1 del usuario 2 en S3
upload_file_key = 'Usuarios/'+'2Usuario/'+'PlayLists/' +'playlist 1  usuario 2.json'
client.upload_file('playlist 1  usuario 2.json', BUCKET_NAME, upload_file_key)
#Guardar PlayList 2 del usuario 2 en S3
upload_file_key = 'Usuarios/'+'2Usuario/'+'PlayLists/' +'playlist 2  usuario 2.json'
client.upload_file('playlist 2  usuario 2.json', BUCKET_NAME, upload_file_key)
#Guardar PlayList 3 del usuario 2 en S3
upload_file_key = 'Usuarios/'+'2Usuario/'+'PlayLists/' +'playlist 3  usuario 2.json'
client.upload_file('playlist 3  usuario 2.json', BUCKET_NAME, upload_file_key)
#Guardar PlayList 4 del usuario 2 en S3
upload_file_key = 'Usuarios/'+'2Usuario/'+'PlayLists/' +'playlist 4  usuario 2.json'
client.upload_file('playlist 4  usuario 2.json', BUCKET_NAME, upload_file_key)
#Guardar PlayList 5 del usuario 2 en S3
upload_file_key = 'Usuarios/'+'2Usuario/'+'PlayLists/' +'playlist 5  usuario 2.json'
client.upload_file('playlist 5  usuario 2.json', BUCKET_NAME, upload_file_key)
