from django.shortcuts import render
from django.views.generic import ListView, CreateView

from .models import AuthorModel

class AuthorListView(ListView):
    model = AuthorModel
    context_object_name = 'list_author'
    template_name = "author/author_list.html"



class AuthorCreateView(CreateView):
    model = AuthorModel
    fields = ['first_name','last_name','nationality','birthday','photo']
    #field=('__all__')
    template_name = "author/create_auth.html"


