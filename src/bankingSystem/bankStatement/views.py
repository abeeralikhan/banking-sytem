from django.shortcuts import render
from datetime import date
from dateutil.relativedelta import relativedelta
from .models import TransactionDetails

# BANK STATEMENT VIEWS

def getStartDate(n):
    return date.today() + relativedelta(months=-n)

def index(request):
    context = {}
    if request.method=="POST":
        transactions = TransactionDetails.objects.filter(user_id = request.user)
        context = {'transactions':transactions}
    
    return render(request, 'bankStatement/index.html', context)


