from django.urls import path

from .views import (LoanCreateView,
                    LoanFormView,
                    MultiLoanFormView,
                    LoanListView,
                    PersonCreateView,
                    PersonListView,
                    PersonListAPIView,
                    PersonEditAPIView
                    )

urlpatterns = [
    path('api/person/list/', PersonListAPIView.as_view()),
    path('api/person/edit/<pk>', PersonEditAPIView.as_view()),
    path('personlist/', PersonListView.as_view()),
    path('createperson/', PersonCreateView.as_view()),
    path('loanlist/', LoanListView.as_view()),
    path('createloan/', LoanCreateView.as_view()),
    path('formloan/', LoanFormView.as_view()),
    path('multiformloan/', MultiLoanFormView.as_view()),
]