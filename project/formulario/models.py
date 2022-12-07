from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# class User(models.Model):
#     username = models.CharField(max_length=10)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.CharField(max_length=30)
#     password = models.CharField(max_length=30)


class Portfolio(models.Model):
    photo = models.ImageField() # Pillow is needed
    project_title = models.CharField(max_length=250)
    project_description = models.TextField()
    tags = models.CharField(max_length=20)
    github_project = models.URLField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ip_address = models.CharField(max_length=15)

    def __str__(self) -> str:
        return f'{self.user.username} portfolio project'