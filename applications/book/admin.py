from django.contrib import admin

from .models import BookModel, CategoryModel

#Dentro del administrador NO podemos crear categorías pues no tienen configurados los métodos para usar el treebeard
#Para crear una categoría se debe hacer a traves de el CreateView para hacer su respectiva inclusión en el arbol 
#Solo utilizaremos el administrador para editar y borrar la categoria
@admin.register(BookModel, CategoryModel)
class MyAdmin(admin.ModelAdmin):
    pass

