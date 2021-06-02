
from django.views.generic import ListView, CreateView

from .models import PersonModel, LoanModel

class PersonCreateView(CreateView):
    model = PersonModel
    context_object_name = 'create_person'
    fields = ['first_name', 'last_name', 'nit','birthday', 'photo']
    template_name = "person/create_person.html"
    success_url = '.'

class PersonListView(ListView):
    model = PersonModel
    context_object_name = 'list_person'
    template_name = "person/list_person.html"

class LoanCreateView(CreateView):
    model = LoanModel
    context_object_name = 'create_loan'
    fields = ['reader','book','loan_date']
    template_name = "person/create_loan.html"
    success_url = '.'

class LoanListView(ListView):
    model = LoanModel
    context_object_name = 'list_loan'
    template_name = "person/list_loan.html"
