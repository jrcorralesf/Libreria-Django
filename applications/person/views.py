from datetime import datetime

from django.shortcuts import redirect
from django.views.generic import ListView, CreateView , FormView


from .models import PersonModel, LoanModel
from .forms import LoanForm, MultiLoanForm

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
class MultiLoanFormView(FormView):
    form_class = MultiLoanForm 
    template_name = "person/multiform_loan.html"
    success_url = '.'

    def form_valid(self, form):
        person_to_lend=form.cleaned_data['reader']
        selected_books=form.cleaned_data['book_list']
        loan_objects=[]
        for single_book in selected_books:
            print(single_book)
            instance = LoanModel(
                reader=person_to_lend,
                book=single_book,
                loan_date=datetime.now(), 
                restored=False,
            )
            loan_objects.append(instance)
        print(loan_objects)
        for obj in loan_objects:
            obj.save()
        #LoanModel.objects.bulk_create(loan_objects) #NO FUNCIONA para modelos que contienen de varias herencias
        return super(MultiLoanFormView,self).form_valid(form)

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
        '''loan=LoanModel(
            reader=form.cleaned_data['reader'],
            book=form.cleaned_data['book'],
            loan_date=datetime.now(), 
            restored=False
        )
        loan.save()'''

        #manejo de disminucion de stock en la vista 
        '''loan_book=form.cleaned_data['book'] 
        loan_book.stock -= 1 #loan_book.stock= loan_book.stock -1
        loan_book.save()'''
        
        #validación de que una persona pueda pedir el mismo libro dos veces
        obj , created = LoanModel.objects.get_or_create(
            reader=form.cleaned_data['reader'],
            book=form.cleaned_data['book'],
            restored=False,
            defaults = {
                'loan_date':datetime.now() #no valida el tiempo, pero si le añade el valor al campo en caso de crear el prestamo
                }
        )
        if created:
            return super().form_valid(form)
        else:
            return redirect('/') #cambiar a pagina que muestre que ya tenia el mismo libro prestado