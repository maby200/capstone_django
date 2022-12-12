from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Portfolio


#ModelForm sirve para no estar creando nuevamente
# los campos donde se ingresarán
# los datos a la base de datos

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields= [
            'photo',
            'project_title',
            'project_description',
            'tags',
            'github_project',
            ]