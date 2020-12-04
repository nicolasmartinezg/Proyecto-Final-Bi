#!/usr/bin/python3
import requests
import pandas as pd
import json
import boto3
from botocore.client import Config
import os

# credenciales para acceder a la api de Deezer
DEEZER_APP_ID = "446902"
DEEZER_APP_SECRET = "154639e6aa1f2214186f80adbe2d5b3b"
DEEZER_REDIRECT_URI = "http://developers.deezer.com/api"

# POST
auth_response = requests.post(DEEZER_REDIRECT_URI, {
    'grant_type': 'client_credentials',
    'client_id': DEEZER_APP_ID,
    'client_secret': DEEZER_APP_SECRET,
})
'''
# EndPoints de el usuario 1-------------------------------------------------------------------------------------------------------------------

''''''
# credenciales para establecer la conexion con AWS
ACCESS_KEY_ID = "AKIASCCE5URAFIEVDIQA"
ACCESS_SECRET_KEY = "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"
BUCKET_NAME = 'pruebasproyectofinal'
client = boto3.client(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version='s3v4')
)
'''

def guardarDatos(nombre, ruta, ruta2):
    URL_PLAYLIST_1 = "https://api.deezer.com/" + ruta
    lr1 = requests.get(URL_PLAYLIST_1)
    jPlayList1 = lr1.json()

    with open(str(nombre) + '.json', 'w') as e:
        json.dump(jPlayList1, e, indent=4, sort_keys=True)

    upload_file_key = ruta2 + '/' + nombre + '.json'
    print(upload_file_key)
    # client.upload_file('playlist '+str(i)+'.json', BUCKET_NAME, upload_file_key)


id_playList = [['playlist/8416193362/tracks?limit=50', 'usuario/usuario2/playlist', 'playlist 1 usuario2'],
               ['playlist/1098908237/tracks?limit=50', 'usuario/usuario2/playlist', 'playlist 2 usuario2'],
               ['playlist/8311123682/tracks?limit=50', 'usuario/usuario2/playlist', 'playlist 3 usuario2'],
               ['playlist/3114195306/tracks?limit=50', 'usuario/usuario2/playlist', 'playlist 4 usuario2'],
               ['playlist/6750169864/tracks?limit=50', 'usuario/usuario2/playlist', 'playlist 5 usuario2'],
               ['playlist/5982817864/tracks?limit=669', 'usuario/usuario1/playlist', 'playlist 1 usuario1'],
               ['user/4039239222/tracks?limit=1656', 'usuario/usuario2/Canciones Favoritas', 'favoritos user2'],
               ['user/4039239222/artists?limit=41', 'usuario/usuario2/Artistas Favoritas', 'Artistas user2'],
               ['user/2605858862/tracks?limit=901', 'usuario/usuario1/Canciones Favoritas', 'favoritos user1'],
               ['user/2605858862/artists?limit=89', 'usuario/usuario1/Artistas Favoritas', 'Artistas user1'],
               ['user/2605858862/artists?limit=89', 'usuario/usuario1/playlist', 'playlist 2 usuario1'],
               ['playlist/971831493/tracks?limit=475', 'usuario/usuario1/playlist', 'playlist 3 usuario1'],
               ['search/playlist?q=j balvin&limit=300', 'artistas/Jbalvin/playlist', 'playlist Jbalvin'],
               ['artist/4860761/fans?limit=100', 'artistas/Jbalvin/Fans', 'Fans Jbalvin'],
               ['artist/4860761/albums?limit=100', 'artistas/Jbalvin/Albums', 'Albums Jbalvin'],
               ['search?q=j balvin&limit=290', 'artistas/Jbalvin/canciones', 'Canciones Jbalvin'],
               ['artist/1059594/playlists?limit=72', 'artistas/AndresCepeda/Playlists', 'Playlists AndresCepeda'],
               ['artist/1059594/albums?limit=41', 'artistas/AndresCepeda/Albums', 'Albums AndresCepeda'],
               ['search?q= andres cepeda&limit=300', 'artistas/AndresCepeda/Canciones', 'Canciones AndresCepeda'],
               ['artist/1059594/fans?limit=100', 'artistas/AndresCepeda/Fans', 'Fans AndresCepeda'],
               ['artist/160/playlists?limit=100', 'artistas/Shakira/Playlists', 'Playlists Shakira'],
               ['artist/160/albums?limit=44', 'artistas/Shakira/Albums', 'Albums Shakira'],
               ['search?q= shakira&limit=261', 'artistas/Shakira/Canciones', 'Canciones Shakira'],
               ['artist/160/fans?limit=100', 'artistas/Shakira/Fans', 'Fans Shakira'],
               ['artist/7343/playlists?limit=100', 'artistas/CarlosVives/Playlists', 'Playlists CarlosVives'],
               ['artist/7343/albums?limit=43', 'artistas/CarlosVives/Albums', 'Albums CarlosVives'],
               ['search?q= carlos vives&limit=289', 'artistas/CarlosVives/Canciones', 'Canciones CarlosVives'],
               ['artist/7343/fans?limit=100', 'artistas/CarlosVives/Fans', 'Fans CarlosVives'],
               ['artist/12944237/playlists?limit=100', 'artistas/Greecy/Playlists', 'Playlists Greecy'],
               ['artist/12944237/albums?limit=39', 'artistas/Greecy/Albums', 'Albums Greecy'],
               ['search?q= greeicy&limit=294', 'artistas/Greecy/Canciones', 'Canciones Greecy'],
               ['artist/12944237/fans?limit=100', 'artistas/Greecy/Fans', 'Fans Greecy'],
               ['artist/58568762/playlists?limit=100', 'artistas/Camilo/Playlists', 'Playlists Camilo'],
               ['artist/58568762/albums?limit=18', 'artistas/Camilo/Albums', 'Albums Camilo'],
               ['search?q= Camilo&limit=299', 'artistas/Camilo/Canciones', 'Canciones Camilo'],
               ['artist/58568762/fans?limit=100', 'artistas/Camilo/Fans', 'Fans Camilo'],
               ['search?q=bpm_min:120&limit=137', 'busquedas/bpmMin120', 'canciones BPM min120'],
               ['genre', 'Generos', 'Generos Deezer'],
               ['genre/122/artists', 'Generos/Reggaeton/Artistas', 'Artistas Reggaeton'],
               ['genre/122/radios', 'Generos/Reggaeton/Radios', 'Radios Reggaeton'],
               ['genre/132/artists', 'Generos/POP/Artistas', 'Artistas Pop'],
               ['radio/top', 'busquedas/TopRadio', 'Radio Top']]
for i in range(len(id_playList)):
    guardarDatos(id_playList[i][2], id_playList[i][0], id_playList[i][1])
