from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView, TemplateView
from django.template.defaultfilters import slugify

from .models import Portfolio
from .forms import ProjectForm
# from taggit.models import Tag



class ProjectView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
    extra_context = {'projects': Portfolio.objects.all()}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Portfolio.objects.all()
        # context['common_tags']
        return context

# def tagged(request, slug):
#     tag = get_object_or_404(Tag, slug=slug)
#     # Filter Portfolio by tag name  
#     projects = Portfolio.objects.filter(tags=tag)
#     context = {
#         'tag':tag,
#         'projects':projects,
#     }
#     return render(request, 'index.html', context)

class UploadData(LoginRequiredMixin, FormView):
    model = Portfolio
    template_name = "proyectos/create_project.html"
    form_class = ProjectForm

    def form_valid(self, form):
        Portfolio.objects.create(**form.cleaned_data)
        # form.save()
        return redirect('index')

@login_required
def deleteProject(request, id):
    project = Portfolio.objects.get(id=id)
    project.delete()
    return redirect('index')



# @login_required
# def upload_data(request):
#     form = ProjectForm(request.POST,request.FILES)
#     if form.is_valid():
#         portfolio = Portfolio(photo = request.FILES['photo'])

#     pass