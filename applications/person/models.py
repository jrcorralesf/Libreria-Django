from django.db import models
from django.db.models.signals import post_delete

from applications.utils.base_model import GeneralModel
from applications.book.models import BookModel
from .managers import PersonManager, LoanManager
class PersonModel(GeneralModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nit = models.PositiveIntegerField()
    birthday = models.DateField(auto_now=False, auto_now_add=False)
    photo = models.ImageField(upload_to='foto_lectores', null=True, blank=True)

    objects = PersonManager()
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

    objects=LoanManager()
    class Meta:
        verbose_name = 'Préstamo'
        verbose_name_plural = 'Préstamos'

    def __str__(self):
        return f'Libro prestado: {self.book.title} | a la persona: {self.reader.first_name} {self.reader.last_name}'

    def save(self, *args, **kwargs):
        #disminución de stock desde el metodo del modelo 
        self.book.stock -= 1
        self.book.save() #usa el metodo sabe del modelo de libro
        return super(LoanModel, self).save(*args, **kwargs)

def restore_book(sender, instance, **kwargs):
    instance.book.stock += 1
    instance.book.save()

post_delete.connect(restore_book, sender= LoanModel)