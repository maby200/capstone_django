from django.db import models
from django.contrib.auth.models import User
# from taggit.managers import TaggableManager

''' WARNING: para usar taggit.managers:
# 1: pip install django-taggit
# 2: settings.py -> INSTALLED_APPS = [...,'taggit',...]
# 3: python manage.py makemigrations, then migrate
# 4: importa aquí '''


class Portfolio(models.Model):
    photo = models.ImageField() # Pillow is needed
    project_title = models.CharField(max_length=250,default='project title')
    project_description = models.TextField(default='Another project')
    # slug = models.SlugField(unique=True, max_length=100)
    tags = models.CharField(max_length=250,default='html, css, django')
    github_project = models.URLField(default='https://github.com/maby200/')
    #hacer que agarre automaticamente el usuario que ha iniciado sesion:
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ip_address = models.CharField(max_length=15, default='127.0.0.1')

    def __str__(self) -> str:
        return f'{self.user.username} portfolio project'