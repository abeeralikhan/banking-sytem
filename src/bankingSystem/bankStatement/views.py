from django.shortcuts import render
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from .models import TransactionDetails

# BANK STATEMENT VIEWS

def getStartDate(n):
    return date.today() + relativedelta(months=-n)

def index(request):
    context = {}
    if request.method=="POST":
        checkForCustomDate = request.POST['radio_month']

        if checkForCustomDate=="True":
            startDate = request.POST['startDate']
            endDate = request.POST['endDate']
            
        else:
            months = checkForCustomDate
            startDate = getStartDate(int(months))
            now = datetime.now()
            endDate = now.strftime("%Y-%m-%d")

        transactions = TransactionDetails.objects.filter(user_id = request.user, tr_date__gte=startDate, tr_date__lte=endDate)
        transactions = transactions.order_by('tr_date')
        context = {'transactions':transactions, 'date1':startDate, 'date2':endDate, 'something':checkForCustomDate}
    
    return render(request, 'bankStatement/index.html', context)


