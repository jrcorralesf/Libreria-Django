
from django.db import models

class PersonManager(models.Manager):
    
    def search_person_by_name(self,kword):
        queryset=self.filter(first_name__icontains=kword )
        return queryset 

class LoanManager(models.Manager):
    pass
    