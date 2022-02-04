from django.shortcuts import render
from .forms import LoanForm
# LOAN APP VIEWS

def index(request):
    return render(request, 'loan/index.html')

def request_loan(request):
    form = LoanForm()
    context = {'form': form}
    return render(request, 'loan/request_loan.html', context)
