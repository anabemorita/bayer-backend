# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from uuid import uuid4

# Create your models here.

class Books(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    ano_de_lancamento = models.IntegerField()
    paginas = models.IntegerField()
    editora = models.CharField(max_length=255)
    descricao = models.TextField()
    disponivel = models.BooleanField()
    data_de_criacao = models.DateField(auto_now_add=True)
