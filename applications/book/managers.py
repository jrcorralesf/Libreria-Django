
from django.db import models
from django.db.models.aggregates import Count

class BookManager(models.Manager):
    
    def search_book_by_name(self,kword):
        queryset=self.filter(name__icontains=kword )
        return queryset 
    
    def search_book_by_categ(self,kword):
        queryset=self.filter(category__name__icontains=kword)
        return queryset 

    #muestra la cantidad de prestamos de cada libro
    def count_books_loan(self):
        result=self.annotate(total=Count('book_loan'))
        for element in result:
            print('---------')
            print(element, element.total)
        return result

class CategoryManager(models.Manager):
    
    def search_categ_by_auth(self,kword):
        #opción de búsqueda con el related_name del ForeignKey del modelo libro
        queryset=self.filter(book_categ__authors__first_name__icontains=kword).distinct()
        return queryset 
    