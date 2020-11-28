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


#credenciales para establecer la conexion con AWS
ACCESS_KEY_ID =  "AKIASCCE5URANBAUR4MU"
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