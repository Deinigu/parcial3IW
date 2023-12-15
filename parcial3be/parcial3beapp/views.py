from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import pymongo
import cloudinary
import cloudinary.uploader

from datetime import datetime

from bson import ObjectId
from rest_framework.response import Response

from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status

from pymongo import ReturnDocument

from google.oauth2 import id_token
from google.auth.transport import requests

from parcial3beapp.serializers import PruebaSerializer, TokenSerializer

# ----------------------------------------  VISTAS DE LA APLICACIÓN ------------------------------
# Conexión a la base de datos MongoDB
my_client = pymongo.MongoClient(
    "mongodb+srv://usuario:usuario@deltacluster.tk2l1kw.mongodb.net/?retryWrites=true&w=majority"
)

# Nombre de la base de datos
dbname = my_client["Parcial3DB"]

# Colecciones
collection_prueba = dbname["prueba"]

# --------- CRUD DE OBJETOS --------
@api_view(['GET', 'POST'])
def prueba_view(request):
    if request.method == 'GET':
        prueba = list(collection_prueba.find({}))        
        for p in prueba:
            p['_id'] = str(ObjectId(p.get('_id',[])))
            p['objid'] = str(ObjectId(p.get('objid',[])))

        prueba_serializer = PruebaSerializer(data=prueba, many= True)
        if prueba_serializer.is_valid():
            json_data = prueba_serializer.data
            return Response(json_data, status=status.HTTP_200_OK)
        else:
            return Response(prueba_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    elif request.method == 'POST':
        serializer = PruebaSerializer(data=request.data)
        if serializer.is_valid():
            prueba = serializer.validated_data
            #Probablemente esto se use para el oauth
            # existing_user = collection_prueba.find_one({'_id': prueba['_id']})
            # if existing_user is not None:
            #     return Response({"error": "Ya existe un usuario con ese correo."},
            #                     status=status.HTTP_400_BAD_REQUEST)
            prueba['_id'] = ObjectId()
            prueba['date'] = datetime.now()
            prueba['array'] = []
            prueba['objid'] = ObjectId(prueba['objid'])
            result = collection_prueba.insert_one(prueba)
            if result.acknowledged:
                return Response({"message": "Objeto creado con éxito."}, status=status.HTTP_201_CREATED)
            else:
                return Response({"error": "Algo salió mal. Objeto no creado."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT', 'DELETE'])
def prueba_detail_view(request, idp):
    if request.method == 'PUT':
        serializer = PruebaSerializer(data=request.data)
        if serializer.is_valid():
            prueba = serializer.validated_data
            prueba['_id'] = ObjectId(idp)
            result = collection_prueba.replace_one({'_id': ObjectId(idp)}, prueba)
            if result.acknowledged:
                return Response({"message": "Objeto actualizado con éxito",},
                                status=status.HTTP_200_OK)
            else:
                return Response({"error": "Algo salió mal. Objeto no actualizado."},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    elif request.method == 'GET':
            p = collection_prueba.find_one({'_id': ObjectId(idp)})
            p['_id'] = str(ObjectId(p.get('_id', [])))
            p['objid'] = str(ObjectId(p.get('objid', [])))

            serializer = PruebaSerializer(data=p)
            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    elif request.method == 'DELETE' :
        delete_data = collection_prueba.delete_one({'_id': ObjectId(idp)})
        if delete_data.deleted_count == 1:
            return Response({"mensaje": "Objeto eliminado con éxito"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Objeto no encontrado"}, status=status.HTTP_404_NOT_FOUND)

# ----------------- OAUTH ----------------
CLIENT_ID = '644438743416-8qs1a5l687337gn7kfmthut9jrvtv1bs.apps.googleusercontent.com'
@api_view(['POST'])
def oauth(request):
    if request.method == 'POST':
        serializer = TokenSerializer(data=request.data)
        if serializer.is_valid():
            tokenData = serializer.validated_data
            try:
                token = tokenData['idtoken']
                # Specify the CLIENT_ID of the app that accesses the backend:
                idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)

                # Or, if multiple clients access the backend server:
                # idinfo = id_token.verify_oauth2_token(token, requests.Request())
                # if idinfo['aud'] not in [CLIENT_ID_1, CLIENT_ID_2, CLIENT_ID_3]:
                #     raise ValueError('Could not verify audience.')

                # If auth request is from a G Suite domain:
                # if idinfo['hd'] != GSUITE_DOMAIN_NAME:
                #     raise ValueError('Wrong hosted domain.')

                # ID token is valid. Get the user's Google Account ID from the decoded token.
                userid = idinfo['sub']
                if userid:
                    return Response({"userid": userid,},
                                    status=status.HTTP_200_OK)
            except ValueError:
                # Invalid token
                return Response({"error": "Token no valido",},
                                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -------------- CLOUDINARY --------------------
@api_view(['POST'])
def upload_image(request):
    if request.method == 'POST' and request.FILES.getlist('images'):
        uploaded_files = request.FILES.getlist('images')
        uploaded_urls = []

        # Upload each image to Cloudinary
        cloudinary.config(
                cloud_name="dx4oicqhy",
                api_key="765172224316842",
                api_secret="ojkOD6jTPcuYjU5Z_77do1AI-VY"
            )

        for file in uploaded_files:
            upload_result = cloudinary.uploader.upload(
                file,
                folder='examen_folder'
            )
            uploaded_urls.append(upload_result['secure_url'])
        return JsonResponse({'urls': uploaded_urls})
    return HttpResponse(status=400)