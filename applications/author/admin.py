from django.contrib import admin

from .models import AuthorModel

@admin.register(AuthorModel)
class MyAdmin(admin.ModelAdmin):
    pass