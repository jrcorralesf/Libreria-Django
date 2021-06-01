from django.urls import path

from .views import AuthorListView, AuthorCreateView

urlpatterns = [
    path('authlist/', AuthorListView.as_view()),
    path('createauth/', AuthorCreateView.as_view()),
]