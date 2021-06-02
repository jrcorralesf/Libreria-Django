from django.urls import path

from .views import (LoanCreateView, 
                    LoanListView,
                    PersonCreateView,
                    PersonListView
                    )

urlpatterns = [
    path('personlist/', PersonListView.as_view()),
    path('createperson/', PersonCreateView.as_view()),
    path('loanlist/', LoanListView.as_view()),
    path('createloan/', LoanCreateView.as_view()),
]