from django.db import models

class BookManager(models.Manager):
    
    def search_book_by_name(self,kword):
        queryset=self.filter(name__icontains=kword )
        return queryset 
    
    def search_book_by_categ(self,kword):
        queryset=self.filter(category__name__icontains=kword)
        return queryset 


class CategoryManager(models.Manager):
    pass
    