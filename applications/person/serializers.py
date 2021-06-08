
from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination

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

class ShortResultsSetPagination(PageNumberPagination):
    page_size = 3 #objetos en la pagina
    page_size_query_param = 'page_size'
    max_page_size = 100 #objetos a cargar en memoria
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000
class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000