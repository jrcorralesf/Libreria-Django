
from django import forms

from .models import LoanModel

class LoanForm(forms.ModelForm):
    
    class Meta:
        model = LoanModel
        fields = ('reader','book')
