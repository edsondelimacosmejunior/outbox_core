__author__ = "Edson de Lima Cosme Junior"
__copyright__ = "Copyright 2018, Edson Junior"
__credits__ = ["Outbox Sistemas"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Edson de Lima Cosme Junior"
__email__ = "edson.junior@outboxsistemas.com"
__status__ = "Production"

from django.db import models
from .cidade import Cidade
from .estado import Estado
from .pais import Pais


class Endereco(models.Model):
    """
    Classe Endereco armazena os dados genéricos de endereços e suas funcionalidades.

    Armazena dos dados básicos, realiza consultas de CEP e todas as funcionalidades referentes a endereços.
    """

    logradouro = models.CharField(
        max_length=250,
        null=False,
        verbose_name="Logradouro"
    )

    numero = models.CharField(
        max_length=10,
        verbose_name="Número"
    )

    cep = models.CharField(
        max_length=9,
        verbose_name="CEP"
    )

    bairro = models.CharField(
        max_length=250,
        verbose_name="Bairro"
    )

    cidade = models.ForeignKey(
        Cidade,
        on_delete=models.CASCADE,
        verbose_name="Cidade"
    )

    estado = models.ForeignKey(
        Estado,
        on_delete=models.CASCADE,
        verbose_name="Estado"
    )

    pais = models.ForeignKey(
        Pais,
        on_delete=models.CASCADE,
        verbose_name="País"
    )

    def __str__(self):
        return self.logradouro

    class Meta:
        app_label = "outbox_core"
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"
