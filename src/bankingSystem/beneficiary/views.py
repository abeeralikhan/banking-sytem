from django.shortcuts import render

# BENEFICIARY APP VIEWS

def index(request):
    return render(request, 'beneficiary/index.html')
