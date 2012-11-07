#-*- coding: utf-8 -*-

from django.db import models


class Estabelecimento(models.Model):
    id_estabelecimento = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    # entrada = INT NULL ,
    # saida = INT NULL ,
    endereco = models.CharField(max_length=150)

    def __unicode__(self):
        return self.nome

    def obtem_vagas_ocupadas(self):
        pass

    # class Meta:
    #     verbose_name = u'palavra-chave'
    #     verbose_name_plural = u'palavras-chave'
    #     db_table = 'palavrachave_palavrachave'
    #     app_label = 'palavra_chave'
