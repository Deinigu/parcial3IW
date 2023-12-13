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

# ----------------------------------------  VISTAS DE LA APLICACIÓN ------------------------------
# Conexión a la base de datos MongoDB
my_client = pymongo.MongoClient(
    "mongodb+srv://usuario:usuario@deltacluster.tk2l1kw.mongodb.net/?retryWrites=true&w=majority"
)

# Nombre de la base de datos
dbname = my_client["Parcial3DB"]

# Colecciones
#collection_prueba = dbname["prueba"]

# CLOUDINARY
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