from django.shortcuts import render

# FUNDS TRANSFER APP VIEWS

def index(request):
    return render(request, 'fundsTransfer/index.html')
