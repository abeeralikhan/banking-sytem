from django.contrib import admin
from django.urls import path, include
from .views import index, dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="banking-system-home"),
    path('dashboard/', dashboard, name='dashboard'),
    path('bankStatement', include('bankStatement.urls')),
    path('loan', include('loan.urls')),
]
