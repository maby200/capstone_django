from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Portfolio



class NewUserForm(UserCreationForm):
    email = forms.EmailField

    class Meta:
        model = User
        fields = ["username","first_name", "last_name", "email", "password1", "password2"]



class ProjectForm(forms.Form):
    class Meta:
        model = Portfolio
        fields=['photo','project_title','project_description', 'tags', 'github_project', 'ip_address']