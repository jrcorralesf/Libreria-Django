
from rest_framework import serializers

from .models import PersonModel, LoanModel

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonModel
        fields = ['id','first_name', 'last_name', 'nit','birthday', 'photo']
        #fields = '__all__'
        #depth = 1


class LoanSerializer(serializers.ModelSerializer):

    class Meta:
        model = LoanModel
        fields = ['reader','book']
        #extra_kwargs= {
        #    'reader': {'viewname'}
        #}