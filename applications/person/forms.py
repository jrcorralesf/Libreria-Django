
from django import forms

from .models import LoanModel
from applications.book.models import BookModel

class MultiLoanForm(forms.ModelForm):

    book_list = forms.ModelMultipleChoiceField(
        queryset=BookModel.objects.all(),
        required=True, 
        widget=forms.CheckboxSelectMultiple,
        )
    class Meta:
        model = LoanModel
        fields = ('reader',)

    #constructor para inicializar valores, de esta manera no se requiere el queryset en el ModelMultipleChoiceField
    '''def __init__(self, *args, **kwargs):
        super(MultiLoanForm, self).__init__(*args, **kwargs)
        self.fields['book_list'].queryset=BookModel.objects.all()'''
class LoanForm(forms.ModelForm):
    class Meta:
        model = LoanModel
        fields = ('reader','book')




    
    