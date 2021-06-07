
from rest_framework import serializers

from .models import PersonModel

class PersonSerializer(serializers.ModelSerializer):
  class Meta:
    model = PersonModel
    fields = ['first_name', 'last_name', 'nit','birthday', 'photo']
    #fields = '__all__'
    #depth = 1
