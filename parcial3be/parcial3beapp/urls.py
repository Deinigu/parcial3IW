from django.urls import path
from parcial3beapp import views

urlpatterns = [

    # PUJAS
    path('api/image/upload', views.upload_image),
    path('logged', views.oauth)
]