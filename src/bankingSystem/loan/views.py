from django.shortcuts import render

# LOAN APP VIEWS

def index(request):
    return render(request, 'loan/index.html')
