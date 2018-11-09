from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Pais


class PaisList(ListView):
    model = Pais