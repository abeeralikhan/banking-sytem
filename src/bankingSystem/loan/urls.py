from django.urls import path
from . import views

# LOAN APP URLS

urlpatterns = [
    path('', views.index, name="loanHome"),
    path('/request_loan', views.request_loan, name="requestLoan")
]