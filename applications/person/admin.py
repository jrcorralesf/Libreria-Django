from django.contrib import admin

from .models import PersonModel, LoanModel

@admin.register(PersonModel, LoanModel)
class MyAdmin(admin.ModelAdmin):
    pass