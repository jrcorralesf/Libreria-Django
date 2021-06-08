from django.urls import path

from .views import (LoanCreateView,
                    LoanFormView,
                    MultiLoanFormView,
                    LoanListView,
                    LoanListAPIView,
                    PersonCreateView,
                    PersonListView,
                    PersonListAPIView,
                    PersonEditAPIView
                    )

app_name='person_app'

urlpatterns = [
    path('api/person/list/', PersonListAPIView.as_view()),
    path('api/person/edit/<pk>/', PersonEditAPIView.as_view(), name='single_person'),
    path('api/loan/list/', LoanListAPIView.as_view()),

    path('personlist/', PersonListView.as_view()),
    path('createperson/', PersonCreateView.as_view()),
    path('loanlist/', LoanListView.as_view()),
    path('createloan/', LoanCreateView.as_view()),
    path('formloan/', LoanFormView.as_view()),
    path('multiformloan/', MultiLoanFormView.as_view()),
]