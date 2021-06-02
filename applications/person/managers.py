
from django.db import models
from django.db.models.aggregates import Count

class PersonManager(models.Manager):
    
    def search_person_by_name(self,kword):
        queryset=self.filter(first_name__icontains=kword )
        return queryset 

class LoanManager(models.Manager):
    
    #agrupa la búsqueda en un diccionario, seleccionando los libros por separado evitando que se agrupen por id del prestamo
    def count_books_loan(self):
        result=self.values('book').annotate(total=Count('book'), title='book__title')
        for element in result:
            print('---------')
            print(element, element['total'])
        return result
    