from django.db.models import query
from django.shortcuts import render
from django.views.generic import ListView, CreateView

from .models import AuthorModel

class AuthorListView(ListView):
    #model = AuthorModel   #se usa sin sobreescribir el get_queryset - retorna todos los objetos del modelo
    context_object_name = 'list_author'
    template_name = "author/author_list.html"
    
    def get_queryset(self):
        catch_name=self.request.GET.get('search_name','')
        return AuthorModel.objects.search_auth(catch_name) #misma funcionalidad a traves de managers
        #queryset=AuthorModel.objects.filter(first_name__icontains=catch_name ) | AuthorModel.objects.filter(last_name__icontains=catch_name)
        #return queryset



class AuthorCreateView(CreateView):
    model = AuthorModel
    fields = ['first_name','last_name','nationality','birthday','photo']
    #field=('__all__')
    template_name = "author/create_auth.html"


