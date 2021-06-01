from django.shortcuts import render
from django.views.generic import ListView

from .models import AuthorModel

class AuthorListView(ListView):
    model = AuthorModel
    context_object_name = 'list_author'
    template_name = "author/author_list.html"

