from django.urls import path

from .views import (CategoryCreateView, 
                    CategoryListView,
                    BookCreateView,
                    BookListView,
                    BookDetailView )

urlpatterns = [
    path('categlist/', CategoryListView.as_view()),
    path('createcateg/', CategoryCreateView.as_view()),
    path('booklist/', BookListView.as_view()),
    path('createbook/', BookCreateView.as_view()),
    path('bookdetails/<pk>/', BookDetailView.as_view(), name='details_of_books'),
]