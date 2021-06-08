
from rest_framework import serializers

from .models import PersonModel, LoanModel

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonModel
        fields = ['id','first_name', 'last_name', 'nit','birthday', 'photo']
        #fields = '__all__'
        #depth = 1


class LoanSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = LoanModel
        fields = ['reader',]
        #fields = ['reader','book'] #se debe crear la vista y el url de detalle para ver e libro
        extra_kwargs= {
                'reader': {'view_name': 'person_app:single_person', 'lookup_field': 'pk'},
        }