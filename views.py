from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Pais


class PaisList(ListView):
    model = Pais
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(PaisList, self).get_context_data(**kwargs)
        context.update({
            'title': "Países",
            'subtitle': "Listagem dos Paises"})
        return context


class PaisCreate(CreateView):
    model = Pais
    fields = ['nome', 'codigo', 'codigo_bc']
    success_url = reverse_lazy('pais_list')

    def get_context_data(self, **kwargs):
        context = super(PaisCreate, self).get_context_data(**kwargs)
        context.update({
            'title': "Países",
            'subtitle': "Listagem dos Paises"})
        return context