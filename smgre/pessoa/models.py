#-*- coding: utf-8 -*-

from django.db import models

class Pessoa(models.Model):
    
    id_pessoa = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=150)
    data_nascimento = models.DateTimeField()
    
    def __unicode__(self):
        return self.nome


    # class Meta:
    #     verbose_name = u'palavra-chave'
    #     verbose_name_plural = u'palavras-chave'
    #     db_table = 'palavrachave_palavrachave'
    #     app_label = 'palavra_chave'

class Responsavel(Pessoa):
    
    id_responsavel = models.AutoField(primary_key=True)
    cargo = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.nome

    # class Meta:
    #     verbose_name = u'palavra-chave'
    #     verbose_name_plural = u'palavras-chave'
    #     db_table = 'palavrachave_palavrachave'
    #     app_label = 'palavra_chave'