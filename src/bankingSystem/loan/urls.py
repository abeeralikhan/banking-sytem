from xml.etree.ElementInclude import include
from django.urls import path, include
from .views import index

# LOAN APP URLS

urlpatterns = [
    path('', index, name="loanHome")
]