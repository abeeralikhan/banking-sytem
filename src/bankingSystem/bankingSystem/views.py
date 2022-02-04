from django.shortcuts import render, redirect

# BANKING SYSTEM PROJECT'S VIEWS
def index(request):
    return redirect ('/dashboard')

def dashboard(request):
    context = {'name': 'Abeer Khan'}
    return render(request, 'index.html', context)