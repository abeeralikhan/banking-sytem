from django.shortcuts import render, redirect

# BANKING SYSTEM PROJECT'S VIEWS
def index(request):
    return redirect ('/dashboard')

def dashboard(request):
    username = request.user
    context = {'name': username}
    return render(request, 'index.html', context)