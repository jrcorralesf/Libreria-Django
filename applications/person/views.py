from datetime import datetime

from django.views.generic import ListView, CreateView , FormView


from .models import PersonModel, LoanModel
from .forms import LoanForm

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

class LoanFormView(FormView):
    form_class = LoanForm
    template_name = "person/form_loan.html"
    success_url = '.'

    def form_valid(self, form):
        
        #opción de guardar usando el método create()
        '''LoanModel.objects.create(
            reader=form.cleaned_data['reader'],
            book=form.cleaned_data['book'],
            loan_date=datetime.now(), 
            restored=False
        )'''

        #opción de guardar usando el método save()
        loan=LoanModel(
            reader=form.cleaned_data['reader'],
            book=form.cleaned_data['book'],
            loan_date=datetime.now(), 
            restored=False
        )
        loan.save()

        #manejo de disminucion de stock en la vista 
        '''loan_book=form.cleaned_data['book'] 
        loan_book.stock -= 1 #loan_book.stock= loan_book.stock -1
        loan_book.save()'''
        

        return super().form_valid(form)

class LoanListView(ListView):
    model = LoanModel
    context_object_name = 'list_loan'
    template_name = "person/list_loan.html"
