from django.db import models

class AuthNameManager(models.Manager):
    
    def search_auth(self,kword):
        queryset=self.filter(first_name__icontains=kword ) | self.filter(last_name__icontains=kword)
        return queryset 