from django.urls import path
from django.views.decorators.cache import cache_page
from . import views

urlpatterns = [
    path('', views.ProjectView.as_view(), name='index'),
    path('upload-project/', views.UploadData.as_view(), name='upload-data'),
    path('delete/<int:id>', views.deleteProject, name='delete'),
]