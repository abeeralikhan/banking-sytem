from xml.etree.ElementInclude import include
from django.urls import path, include
from .views import index

urlpatterns = [
    path('', index, name="loanHome")
]