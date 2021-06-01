from django.db import models

from applications.utils.base_model import GeneralModel
from applications.book.models import BookModel
class PersonModel(GeneralModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nit = models.SmallIntegerField()
    birthday = models.DateField(auto_now=False, auto_now_add=False)
    photo = models.ImageField(upload_to='foto_lectores', null=True, blank=True)
    class Meta:
        verbose_name = 'Lector'
        verbose_name_plural = 'Lectores'
        ordering = ['last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class LoanModel(GeneralModel):
    reader=models.ForeignKey(PersonModel,related_name='reader_loan', on_delete=models.CASCADE)
    book=models.ForeignKey(BookModel,related_name='book_loan', on_delete=models.CASCADE)
    loan_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    restore_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    restored= models.BooleanField()
    class Meta:
        verbose_name = 'Préstamo'
        verbose_name_plural = 'Préstamos'

    def __str__(self):
        return f'Libro prestado: {self.book.title}'
