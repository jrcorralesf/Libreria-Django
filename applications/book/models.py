
from django.db import models
from treebeard.mp_tree import MP_Node

from applications.utils.base_model import GeneralModel
from applications.author.models import AuthorModel

class CategoryModel(GeneralModel, MP_Node):
    name = models.CharField(max_length=150)
    description = models.TextField(help_text="Descripción corta", null=True, blank=True)
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return f'Categoría: {self.name} {self.path}'


class BookModel(GeneralModel):
    title = models.CharField(max_length=150)
    resume = models.TextField(help_text="Resumen", null=True, blank=True)
    publication_date = models.DateField(auto_now=False, auto_now_add=False)
    authors = models.ManyToManyField(AuthorModel)
    cover_page = models.ImageField(upload_to='portadas', null=True, blank=True)
    category=models.ForeignKey('book.CategoryModel',related_name='book_categ', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

    def __str__(self):
        return f'Libro: {self.title}'