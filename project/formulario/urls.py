from django.contrib import admin
from django.urls import path
from .views import register, upload_data


urlpatterns = [
    path('', register, name='register' ),
    path('upload-project/', upload_data, name='upload-data' ),
]