from django.contrib import admin
from django.urls import path, include
from .views import index, dashboard

# BANKING SYSTEM PROJECT'S URLS

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="banking-system-home"),
    path('dashboard/', dashboard, name='dashboard'),
    path('bankStatement', include('bankStatement.urls')),
    path('loan', include('loan.urls')),
    path('beneficiary', include('beneficiary.urls')),
    path('fundsTransfer', include('fundsTransfer.urls')),
    path('login', include('login.urls')),
]
