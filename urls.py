from django.urls import path
from .views import PaisList, PaisCreate

urlpatterns = [
    path('pais/', PaisList.as_view(), name='pais_list'),
    path('pais/create/', PaisCreate.as_view(), name='pais_create')
]