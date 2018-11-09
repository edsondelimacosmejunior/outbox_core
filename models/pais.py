__author__ = "Edson de Lima Cosme Junior"
__copyright__ = "Copyright 2018, Edson Junior"
__credits__ = ["Outbox Sistemas"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Edson de Lima Cosme Junior"
__email__ = "edson.junior@outboxsistemas.com"
__status__ = "Production"

from django.db import models


class Pais(models.Model):
    """
    Classe País armazena os dados de um país.

    Armazena dos dados básicos, como nome e código, a dados que podem ser usados por outros módulos como o código BC.
    """

    nome = models.CharField(
        max_length=250,
        null=False,
        verbose_name="Nome"
    )

    codigo_bc = models.CharField(
        max_length=5,
        verbose_name="Código BC"
    )

    codigo = models.CharField(
        max_length=2,
        verbose_name="Código do País"
    )

    def __str__(self):
        return self.nome

    class Meta:
        app_label = "outbox_core"
        verbose_name = "País"
        verbose_name_plural = "Países"
        ordering = ['nome']
