from django.urls import path
from .views import index

# BENEFICIARY APP URLS

urlpatterns = [
    path('', index, name="beneficiaryHome")
]