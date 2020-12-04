
import json
import boto3

s3 = boto3.resource('s3')


def lambda_handler(event, context):
    bucket = 'pruebasproyectofinal'

    keyA = ['Artistas/AndresCepeda/Albums/albums AndresCepeda.json',
            'Artistas/Camilo/Albums/albums Camilo.json',
            'Artistas/CarlosVives/Albums/albums Carlos Vives.json',
            'Artistas/Greeicy/Albums/albums Greeicy.json',
            'Artistas/JBalvin/Albums/Album J Balvin.json',
            'Artistas/Shakira/Albums/albums Shakira.json',
            'Artistas/AndresCepeda/PlayList/playlist AndresCepeda.json',
            'Artistas/Camilo/PlayList/playlist Camilo.json',
            'Artistas/CarlosVives/PlayList/playlist Carlos Vives.json',
            'Artistas/Greeicy/PlayList/playlist Greeicy.json',
            'Artistas/JBalvin/PlayList/PlayList JBalvin.json',
            'Artistas/Shakira/PlayList/playlist Shakira.json',
            'Busquedas/topRadio/top Radio.json']

    keyF = ['Artistas/AndresCepeda/Fans/fans AndresCepeda.json',
            'Artistas/Camilo/Fans/fans Camilo.json',
            'Artistas/CarlosVives/Fans/fans Carlos.json',
            'Artistas/Greeicy/Fans/fans Greeicy.json',
            'Artistas/JBalvin/Fans/fans J Balvin.json',
            'Artistas/Shakira/Fans/fans Shakira.json',
            'Generos/Pop/Artistas/Artistas Pop.json',
            'Generos/Reggaeton/Artistas/Artistas Reggaeton.json',
            'Generos/Generos Deezer.json']

    keyC = ['Usuarios/2Usuario/PlayLists/playlist 1  usuario 2.json',
            'Usuarios/2Usuario/PlayLists/playlist 2  usuario 2.json',
            'Usuarios/2Usuario/PlayLists/playlist 3  usuario 2.json',
            'Usuarios/2Usuario/PlayLists/playlist 4  usuario 2.json',
            'Usuarios/2Usuario/PlayLists/playlist 5  usuario 2.json']
    for i in keyC:
        leerJsonCanciones(i, bucket)
    for fans in keyF:
        leerJsonFans(fans, bucket)
    for album in keyA:
        leerJsonAlbum(album, bucket)


def leerJsonCanciones(key, bucket):
    obj = s3.Object(bucket, key)
    data = obj.get()['Body'].read().decode('utf-8')
    json_data = json.loads(data)
    for i in json_data['data']:
        print(i['artist']['name'], i['album']['title'], i['type'], i['title'], i['duration'])


def leerJsonAlbum(key, bucket):
    obj = s3.Object(bucket, key)
    data = obj.get()['Body'].read().decode('utf-8')
    json_data = json.loads(data)
    for i in json_data['data']:
        print(i['id'], i['title'], i['type'])


def leerJsonFans(key, bucket):
    obj = s3.Object(bucket, key)
    data = obj.get()['Body'].read().decode('utf-8')
    json_data = json.loads(data)
    for i in json_data['data']:
        print(i['id'], i['name'], i['type'])




