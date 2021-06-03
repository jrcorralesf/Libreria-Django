
from django.db import models
from django.db.models.deletion import CASCADE
from treebeard.mp_tree import MP_Node

from applications.utils.base_model import GeneralModel
from applications.author.models import AuthorModel
from .managers import BookManager, CategoryManager

class CategoryModel(MP_Node, GeneralModel):
    name = models.CharField(max_length=150)
    description = models.TextField(help_text="Descripción corta", null=True, blank=True)
    parent_category = models.ForeignKey('self', related_name='related_categ', blank=True, null=True , on_delete=CASCADE)
    
    objects=CategoryManager()
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
    stock = models.PositiveIntegerField(default=0)

    objects = BookManager()
    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

    def __str__(self):
        return f'Libro: {self.title} | cantidad restante: {self.stock}'
