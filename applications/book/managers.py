
from django.db import models
from django.db.models.aggregates import Count
from django.contrib.postgres.search import TrigramSimilarity


class BookManager(models.Manager):
    
    def search_book_by_title(self,kword):
        queryset=self.filter(title__icontains=kword )
        return queryset 

    #utilizando la TrigramSimilarity para que el buscador detecte la mejor similitud
    def search_book_by_title_trg(self,kword):
        if len(kword)>=3: #el trigram solo funciona si se pasan más de 3 caracteres
            return self.filter(title__trigram_similar=kword )
        else:
            return self.all()[:10] 

    def search_book_by_pubdate(self):
        queryset=self.filter(publication_date__range=('1800-01-01', '2000-01-01'))
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
    