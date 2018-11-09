__author__ = "Edson de Lima Cosme Junior"
__copyright__ = "Copyright 2018, Edson Junior"
__credits__ = ["Outbox Sistemas"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Edson de Lima Cosme Junior"
__email__ = "edson.junior@outboxsistemas.com"
__status__ = "Production"

from django.db import models
from .pais import Pais


class Estado(models.Model):
    """
    Classe Estado armazena os estados das federações.

    Armazena dos dados básicos, como nome e UF, a dados que podem ser usados por outros módulos como o código IBGE.
    """

    nome = models.CharField(
        max_length=250,
        null=False,
        verbose_name="Nome"
    )

    uf = models.CharField(
        max_length=3,
        verbose_name="UF"
    )

    codigo_ibge = models.CharField(
        max_length=2,
        verbose_name="Código IBGE"
    )

    pais = models.ForeignKey(
        Pais,
        on_delete=models.CASCADE,
        verbose_name="País"
    )

    def __str__(self):
        return self.nome

    class Meta:
        app_label = "outbox_core"
        verbose_name = "Estado"
        verbose_name_plural = "Estados"
        ordering = ['nome']
