from django.shortcuts import render

# BANK STATEMENT VIEWS

def index(request):
    return render(request, 'bankStatement/index.html')
