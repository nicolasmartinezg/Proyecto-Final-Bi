#!/usr/bin/python3
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
BASE_URL = 'https://api.deezer.com/search/playlist?q=j balvin&limit=300'
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



#------------------------------------------------------------------------------------------------------------------------------------------------------
#Información del Artista Andres Cepeda

#PlayList
URL_PLAYLIST_ANDRES = "https://api.deezer.com/artist/1059594/playlists?limit=72"
pAndres = requests.get(URL_PLAYLIST_ANDRES)
jpAndres = pAndres.json()
#Guardar playlist
with open('playlist AndresCepeda.json', 'w') as e:
    json.dump(jpAndres, e, indent=4, sort_keys=True)
#Albunes
URL_ALBUM_ANDRES = "https://api.deezer.com/artist/1059594/albums?limit=41"
alAndres = requests.get(URL_ALBUM_ANDRES)
jalAndres = alAndres.json()
#Guardar albums
with open('albums AndresCepeda.json', 'w') as e:
    json.dump(jalAndres, e, indent=4, sort_keys=True)
#Canciones
URL_CANCIONES_ANDRES = "https://api.deezer.com/search?q= andres cepeda&limit=300"
cAndres = requests.get(URL_CANCIONES_ANDRES)
jcAndres = cAndres.json()
#Guardar canciones
with open('canciones AndresCepeda.json', 'w') as e:
    json.dump(jcAndres, e, indent=4, sort_keys=True)
#Fans
URL_FANS_ANDRES = "https://api.deezer.com/artist/1059594/fans?limit=100"
fAndres = requests.get(URL_FANS_ANDRES)
jfAndres = fAndres.json()
#Guardar fans
with open('fans AndresCepeda.json', 'w') as e:
    json.dump(jfAndres, e, indent=4, sort_keys=True)
#-------------------------------------------------------------------------------------------------------------------------------------------------------

#Información de la artista Shakira

#Playlist
URL_PLAYLIST_SHAKIRA = "https://api.deezer.com/artist/160/playlists?limit=100"
pShakira = requests.get(URL_PLAYLIST_SHAKIRA)
jpShakira = pShakira.json()
#Guardar playlist
with open('playlist Shakira.json', 'w') as e:
    json.dump(jpShakira, e, indent=4, sort_keys=True)
#Albums
URL_ALBUM_SHAKIRA = "https://api.deezer.com/artist/160/albums?limit=44"
alShakira = requests.get(URL_ALBUM_SHAKIRA)
jalShakira = alShakira.json()
#Guardar albums
with open('albums Shakira.json', 'w') as e:
    json.dump(jalShakira, e, indent=4, sort_keys=True)
#Canciones
URL_CANCIONES_SHAKIRA = "https://api.deezer.com/search?q= shakira&limit=261"
cShakira = requests.get(URL_CANCIONES_SHAKIRA)
jcShakira= cShakira.json()
#Guardar canciones
with open('canciones Shakira.json', 'w') as e:
    json.dump(jcShakira, e, indent=4, sort_keys=True)
#Fans
URL_FANS_SHAKIRA = "https://api.deezer.com/artist/160/fans?limit=100"
fShakira = requests.get(URL_FANS_SHAKIRA)
jfShakira = fShakira.json()
#Guardar fans
with open('fans Shakira.json', 'w') as e:
    json.dump(jfShakira, e, indent=4, sort_keys=True)

#------------------------------------------------------------------------------------------------------------------------------------------------------
#Información del artista Carlos Vives

#Playlist
URL_PLAYLIST_CARLOS = "https://api.deezer.com/artist/7343/playlists?limit=100"
pCarlos = requests.get(URL_PLAYLIST_CARLOS)
jpCarlos = pCarlos.json()
#Guardar playlist
with open('playlist Carlos Vives.json', 'w') as e:
    json.dump(jpCarlos, e, indent=4, sort_keys=True)
#Albums
URL_ALBUM_CARLOS = "https://api.deezer.com/artist/7343/albums?limit=43"
alCarlos = requests.get(URL_ALBUM_CARLOS)
jalCarlos = alCarlos.json()
#Guardar albums
with open('albums Carlos Vives.json', 'w') as e:
    json.dump(jalCarlos, e, indent=4, sort_keys=True)
#Canciones
URL_CANCIONES_CARLOS = "https://api.deezer.com/search?q= carlos vives&limit=289"
cCarlos = requests.get(URL_CANCIONES_CARLOS)
jcCarlos = cCarlos.json()
#Guardar canciones
with open('canciones Carlos Vives.json', 'w') as e:
    json.dump(jcCarlos, e, indent=4, sort_keys=True)
#Fans
URL_FANS_CARLOS = "https://api.deezer.com/artist/7343/fans?limit=100"
fCarlos = requests.get(URL_FANS_CARLOS)
jfCarlos = fCarlos.json()
#Guardar fans
with open('fans Carlos.json', 'w') as e:
    json.dump(jfCarlos, e, indent=4, sort_keys=True)
#------------------------------------------------------------------------------------------------------------------------------------------------------
#Información de la artista Greeicy

#Playlist
URL_PLAYLIST_GREEICY = "https://api.deezer.com/artist/12944237/playlists?limit=100"
pGreeicy = requests.get(URL_PLAYLIST_GREEICY)
jpGreeicy = pGreeicy.json()
#Guardar playlist
with open('playlist Greeicy.json', 'w') as e:
    json.dump(jpGreeicy, e, indent=4, sort_keys=True)
#Albums
URL_ALBUM_GREEICY = "https://api.deezer.com/artist/12944237/albums?limit=39"
alGreeicy = requests.get(URL_ALBUM_GREEICY)
jalGreeicy = alGreeicy.json()
#Guardar albums
with open('albums Greeicy.json', 'w') as e:
    json.dump(jalGreeicy, e, indent=4, sort_keys=True)
#Canciones
URL_CANCIONES_GREEICY = "https://api.deezer.com/search?q= greeicy&limit=294"
cGreeicy= requests.get(URL_CANCIONES_GREEICY)
jcGreeicy= cGreeicy.json()
#Guardar canciones
with open('canciones Greeicy.json', 'w') as e:
    json.dump(jcGreeicy, e, indent=4, sort_keys=True)
#Fans
URL_FANS_GREEICY = "https://api.deezer.com/artist/12944237/fans?limit=100"
fGreeicy = requests.get(URL_FANS_GREEICY)
jfGreeicy = fGreeicy.json()
#Guardar fans
with open('fans Greeicy.json', 'w') as e:
    json.dump(jfGreeicy, e, indent=4, sort_keys=True)
#------------------------------------------------------------------------------------------------------------------------------------------------------
#Información del artista Camilo

#Playlist
URL_PLAYLIST_CAMILO = "https://api.deezer.com/artist/58568762/playlists?limit=100"
pCamilo = requests.get(URL_PLAYLIST_CAMILO)
jpCamilo = pCamilo.json()
#Guardar playlist
with open('playlist Camilo.json', 'w') as e:
    json.dump(jpCamilo, e, indent=4, sort_keys=True)
#Albums
URL_ALBUM_CAMILO = "https://api.deezer.com/artist/58568762/albums?limit=18"
alCamilo = requests.get(URL_ALBUM_CAMILO)
jalCamilo = alCamilo.json()
#Guardar albums
with open('albums Camilo.json', 'w') as e:
    json.dump(jalCamilo, e, indent=4, sort_keys=True)
#Canciones
URL_CANCIONES_CAMILO = "https://api.deezer.com/search?q= Camilo&limit=299"
cCamilo = requests.get(URL_CANCIONES_CAMILO)
jcCamilo = cCamilo.json()
#Guardar canciones
with open('canciones Camilo.json', 'w') as e:
    json.dump(jcCamilo, e, indent=4, sort_keys=True)
#Fans
URL_FANS_CAMILO = "https://api.deezer.com/artist/58568762/fans?limit=100"
fCamilo = requests.get(URL_FANS_CAMILO)
jfCamilo = fCamilo.json()
#Guardar fans
with open('fans Camilo.json', 'w') as e:
    json.dump(jfCamilo, e, indent=4, sort_keys=True)
#------------------------------------------------------------------------------------------------------------------------------------------------------
#EndPoints para realizar busquedas

#URL para sacar las canciones con un bpm min 120
URL_BPM_MIN120='https://api.deezer.com/search?q=bpm_min:120&limit=137'
bpm= requests.get(URL_BPM_MIN120)
bpm120=bpm.json()
#guardar json
with open('canciones BPM min120.json', 'w') as e:
    json.dump(bpm120, e, indent=4, sort_keys=True)

#Endpoints para consultar los generos, los artistas que pertenecen a un genero, los podcast y la radio
#ENDPOINT QUE ME TRAE TODOS LOS GENEROS DE LA API DEEZER
URL_GENEROS='https://api.deezer.com/genre'
g=requests.get(URL_GENEROS)
GN= g.json()
#guardar json
with open('Generos Deezer.json', 'w') as e:
    json.dump(GN, e, indent=4, sort_keys=True)

#ENDPOINT QUE ME CONSULTA LOS ARTISTAS QUE PERTENECEN AL GENERO REGGAETON
URL_GENEROS_REGGAETON='https://api.deezer.com/genre/122/artists'
rg=requests.get(URL_GENEROS_REGGAETON)
RG= rg.json()
with open('Artistas Reggaeton.json', 'w') as e:
    json.dump(RG, e, indent=4, sort_keys=True)


#ENDPOINT QUE ME CONSULTA LA RADIO QUE PERTENECE AL GENERO REGGAETON
URL_RADIO_REGGAETON='https://api.deezer.com/genre/122/radios'
urr=requests.get(URL_RADIO_REGGAETON)
URR=urr.json()
with open('Radio Reggaeton.json', 'w') as e:
    json.dump(URR, e, indent=4, sort_keys=True)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Endpoint ue me consulta los artistas que pertenecen al genero POP
URL_GENEROS_POP='https://api.deezer.com/genre/132/artists'
rPop=requests.get(URL_GENEROS_POP)
jPop= rPop.json()
with open('Artistas Pop.json', 'w') as e:
    json.dump(jPop, e, indent=4, sort_keys=True)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Endpoint que consulta el top radio de Deezer
URL_RADIO_TOP='https://api.deezer.com/radio/top'
rRadio=requests.get(URL_RADIO_TOP)
jRadio= rRadio.json()
with open('top Radio.json', 'w') as e:
    json.dump(jRadio, e, indent=4, sort_keys=True)

#credenciales para establecer la conexion con AWS
ACCESS_KEY_ID =  ""
ACCESS_SECRET_KEY = ""
#BUCKET_NAME = 'pruebasproyectofinal'
BUCKET_NAME = 'deezer'
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

#--------------------------------------------------------------------------------------------------------------------------------------------------------

#Guardar informacion del artista Andres Cepeda en S3

#Playlists

upload_file_key = 'Artistas/'+'AndresCepeda/'+'PlayList/' + 'playlist AndresCepeda.json'
client.upload_file('playlist AndresCepeda.json', BUCKET_NAME, upload_file_key)

#albums

upload_file_key = 'Artistas/'+'AndresCepeda/'+'Albums/' + 'albums AndresCepeda.json'
client.upload_file('albums AndresCepeda.json', BUCKET_NAME, upload_file_key)

#Canciones

upload_file_key = 'Artistas/'+'AndresCepeda/'+'canciones/' + 'canciones AndresCepeda.json'
client.upload_file('canciones AndresCepeda.json', BUCKET_NAME, upload_file_key)

#Fans

upload_file_key = 'Artistas/'+'AndresCepeda/'+'Fans/' + 'fans AndresCepeda.json'
client.upload_file('fans AndresCepeda.json', BUCKET_NAME, upload_file_key)

#--------------------------------------------------------------------------------------------------------------------------------------------------------

#Guardar informacion del artista Shakira en S3

#Playlists

upload_file_key = 'Artistas/'+'Shakira/'+'PlayList/' + 'playlist Shakira.json'
client.upload_file('playlist Shakira.json', BUCKET_NAME, upload_file_key)

#albums

upload_file_key = 'Artistas/'+'Shakira/'+'Albums/' + 'albums Shakira.json'
client.upload_file('albums Shakira.json', BUCKET_NAME, upload_file_key)

#Canciones

upload_file_key = 'Artistas/'+'Shakira/'+'canciones/' + 'canciones Shakira.json'
client.upload_file('canciones Shakira.json', BUCKET_NAME, upload_file_key)

#Fans

upload_file_key = 'Artistas/'+'Shakira/'+'Fans/' + 'fans Shakira.json'
client.upload_file('fans Shakira.json', BUCKET_NAME, upload_file_key)

#--------------------------------------------------------------------------------------------------------------------------------------------------------

#Guardar informacion del artista Carlos Vives en S3
#Playlists

upload_file_key = 'Artistas/'+'CarlosVives/'+'PlayList/' + 'playlist Carlos Vives.json'
client.upload_file('playlist Carlos Vives.json', BUCKET_NAME, upload_file_key)

#albums

upload_file_key = 'Artistas/'+'CarlosVives/'+'Albums/' + 'albums Carlos Vives.json'
client.upload_file('albums Carlos Vives.json', BUCKET_NAME, upload_file_key)

#Canciones

upload_file_key = 'Artistas/'+'CarlosVives/'+'canciones/' + 'canciones Carlos Vives.json'
client.upload_file('canciones Carlos Vives.json', BUCKET_NAME, upload_file_key)

#Fans

upload_file_key = 'Artistas/'+'CarlosVives/'+'Fans/' + 'fans Carlos.json'
client.upload_file('fans Carlos.json', BUCKET_NAME, upload_file_key)

#--------------------------------------------------------------------------------------------------------------------------------------------------------

#Guardar informacion del artista Greeicy en S3
#Playlists

upload_file_key = 'Artistas/'+'Greeicy/'+'PlayList/' + 'playlist Greeicy.json'
client.upload_file('playlist Greeicy.json', BUCKET_NAME, upload_file_key)

#albums

upload_file_key = 'Artistas/'+'Greeicy/'+'Albums/' + 'albums Greeicy.json'
client.upload_file('albums Greeicy.json', BUCKET_NAME, upload_file_key)

#Canciones

upload_file_key = 'Artistas/'+'Greeicy/'+'canciones/' + 'canciones Greeicy.json'
client.upload_file('canciones Greeicy.json', BUCKET_NAME, upload_file_key)

#Fans

upload_file_key = 'Artistas/'+'Greeicy/'+'Fans/' + 'fans Greeicy.json'
client.upload_file('fans Greeicy.json', BUCKET_NAME, upload_file_key)

#--------------------------------------------------------------------------------------------------------------------------------------------------------

#Guardar informacion del artista Camilo en S3
#Playlists

upload_file_key = 'Artistas/'+'Camilo/'+'PlayList/' + 'playlist Camilo.json'
client.upload_file('playlist Camilo.json', BUCKET_NAME, upload_file_key)

#albums

upload_file_key = 'Artistas/'+'Camilo/'+'Albums/' + 'albums Camilo.json'
client.upload_file('albums Camilo.json', BUCKET_NAME, upload_file_key)

#Canciones

upload_file_key = 'Artistas/'+'Camilo/'+'canciones/' + 'canciones Camilo.json'
client.upload_file('canciones Camilo.json', BUCKET_NAME, upload_file_key)

#Fans

upload_file_key = 'Artistas/'+'Camilo/'+'Fans/' + 'fans Camilo.json'
client.upload_file('fans Camilo.json', BUCKET_NAME, upload_file_key)
#---------------------------------------------------------------------------------------------------
#GUARDAR CONSULTAS ADICIONALES EN S3
#canciones que tienen un bpm min de 120
upload_file_key = 'Busquedas/'+'BPM_MIN_120/'+'canciones BPM min120.json'
client.upload_file('canciones BPM min120.json', BUCKET_NAME, upload_file_key)

#TODOS LOS GENEROS DE LA API
upload_file_key = 'Generos/'+'Generos Deezer.json'
client.upload_file('Generos Deezer.json', BUCKET_NAME, upload_file_key)

#Artistas pertenecientes al genero Regaeton
upload_file_key = 'Generos/'+'Reggaeton/'+'Artistas/'+'Artistas Reggaeton.json'
client.upload_file('Artistas Reggaeton.json', BUCKET_NAME, upload_file_key)

#RADIO QUE PERTENECE AL GENERO REGGAETON
upload_file_key = 'Generos/'+'Reggaeton/'+'Radio/'+'Radio Reggaeton.json'
client.upload_file('Radio Reggaeton.json', BUCKET_NAME, upload_file_key)

#Artistas pertenecientes al genero Pop
upload_file_key = 'Generos/'+'Pop/'+'Artistas/'+'Artistas Pop.json'
client.upload_file('Artistas Pop.json', BUCKET_NAME, upload_file_key)

#Top de radios de Deezer
upload_file_key = 'Busquedas/'+'topRadio/'+'top Radio.json'
client.upload_file('top Radio.json', BUCKET_NAME, upload_file_key)