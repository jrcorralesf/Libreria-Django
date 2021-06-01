
from django.db import models
from django_countries.fields import CountryField

from applications.utils.base_model import GeneralModel

class AuthorModel(GeneralModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nationality = CountryField(blank_label='(seleccione un país)')
    birthday = models.DateField(auto_now=False, auto_now_add=False)
    photo = models.ImageField(upload_to='fotos', null=True, blank=True)
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
