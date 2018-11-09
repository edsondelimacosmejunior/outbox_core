from django.urls import path
from .views import PaisList

urlpatterns = [
    path('pais/', PaisList.as_view(), name='pais_list')
]