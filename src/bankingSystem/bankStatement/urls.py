from django.urls import path
from .views import index

# BANK STATEMENT URLS

urlpatterns = [
    path('/', index, name="home")
]