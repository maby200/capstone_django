from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import Portfolio
from .forms import ProjectForm, NewUserForm

# Create your views here.

def register(request):
    form = NewUserForm(request.POST or None)
    if request.method == "POST":
        
        if form.is_valid():
            # username = form.cleaned_data.get('username')
            # messages.success(request, f'Tu cuenta ha sido creada!')
            form.save()
            # return HttpResponseRedirect('/success/')
        else:
            form = NewUserForm()
    return render(request, 'register_user.html', {'form':form})

@login_required
def upload_data(request):
    form = ProjectForm(request.POST,request.FILES)
    if form.is_valid():
        portfolio = Portfolio(photo = request.FILES['photo'])

    pass
