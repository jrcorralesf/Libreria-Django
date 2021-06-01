from django.urls import path

from .views import AuthorListView

urlpatterns = [
    path('authlist/', AuthorListView.as_view()),
]