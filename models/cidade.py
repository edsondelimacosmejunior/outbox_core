__author__ = "Edson de Lima Cosme Junior"
__copyright__ = "Copyright 2018, Edson Junior"
__credits__ = ["Outbox Sistemas"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Edson de Lima Cosme Junior"
__email__ = "edson.junior@outboxsistemas.com"
__status__ = "Production"

from django.db import models
from .estado import Estado


class Cidade(models.Model):
    """
    Classe Cidade armazena os dados de cidades e municípios.

    Armazena dos dados básicos, como nome e estado, a dados que podem ser usados por outros módulos como o código IBGE.
    """

    nome = models.CharField(
        max_length=250,
        null=False,
        verbose_name="Nome"
    )

    codigo_ibge = models.CharField(
        max_length=7,
        verbose_name="Código IBGE"
    )

    estado = models.ForeignKey(
        Estado,
        on_delete=models.CASCADE,
        verbose_name="Estado"
    )

    def __str__(self):
        return self.nome

    class Meta:
        app_label = "outbox_core"
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"
        ordering = ['nome']
