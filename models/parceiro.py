__author__ = "Edson de Lima Cosme Junior"
__copyright__ = "Copyright 2018, Edson Junior"
__credits__ = ["Outbox Sistemas"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Edson de Lima Cosme Junior"
__email__ = "edson.junior@outboxsistemas.com"
__status__ = "Production"

from django.db import models
from .endereco import Endereco


class Parceiro(Endereco, models.Model):
    """
    Classe Parceiro armazena e controla os dados de parceiros.

    A classe parceiro pode ser utilizada para armazenar dados de pessoas, empresas, clientes, fornecedores. Além de
    ser herdada para ser utilizada em mais uma diversidade de situações, pois implementa regras básicas para todas
    essas situações. Além disso, herda de Endereco para utilizar seus campos e funcionalidades.
    """

    nome = models.CharField(
        max_length=250,
        null=False,
        verbose_name="Nome"
    )

    razao_social = models.CharField(
        max_length=250,
        verbose_name="Razão Social"
    )

    cnpj = models.CharField(
        max_length=18,
        verbose_name="CNPJ"
    )

    cpf = models.CharField(
        max_length=14,
        verbose_name="CPF"
    )

    rg = models.CharField(
        max_length=30,
        verbose_name="RG"
    )

    is_empresa = models.BooleanField(
        verbose_name="É uma empresa?"
    )

    inscricao_estadual = models.CharField(
        max_length=50,
        verbose_name="Inscrição Estadual"
    )

    inscricao_municipal = models.CharField(
        max_length=50,
        verbose_name="Inscrição Municipal"
    )

    celular = models.CharField(
        max_length=30,
        verbose_name="Celular"
    )

    telefone = models.CharField(
        max_length=30,
        verbose_name="Celular"
    )

    email = models.CharField(
        max_length=100,
        verbose_name="E-mail"
    )

    site = models.CharField(
        max_length=100,
        verbose_name="Site"
    )

    data_aniversario = models.DateField(
        verbose_name="Aniversário"
    )

    is_cliente = models.BooleanField(
        verbose_name="É Cliente?"
    )

    is_fornecedor = models.BooleanField(
        verbose_name="É Fornecedor?"
    )

    notas = models.TextField(
        verbose_name="Notas"
    )

    def __str__(self):
        return self.nome

    class Meta:
        app_label = "outbox_core"
        verbose_name = "Parceiro"
        verbose_name_plural = "Parceiros"
        ordering = ['nome']
