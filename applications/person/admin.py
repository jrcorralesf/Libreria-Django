from django.contrib import admin

from .models import PersonModel

@admin.register(PersonModel)
class MyAdmin(admin.ModelAdmin):
    pass