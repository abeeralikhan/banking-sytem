from django.urls import path
from .views import index

# FUNDS TRANSFER APP URLS

urlpatterns = [
    path('', index, name="fundsTransferHome")
]