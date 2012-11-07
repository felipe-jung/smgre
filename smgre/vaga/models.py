from django.db import models
from smgre.pessoa.models import Pessoa

class Tarifa(models.Model):
    id_tarifa = models.AutoField(primary_key=True)
    preco_inicial = models.FloatField()
    carencia = models.IntegerField()
    preco_hora_adicional = models.FloatField()

class TipoVaga(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    tarifa = models.ForeignKey(Tarifa, null=False, blank=False, related_name='tipo_vaga')

    def __unicode__(self):
        return self.nome


class Vaga(models.Model):
    id_vaga = models.AutoField(primary_key=True)
    posicao = models.CharField(u'Nome',max_length=100)
    status = models.BooleanField(null=False, blank=False)
    tipo_vaga = models.ForeignKey(TipoVaga, null=False, blank=False, related_name='vagas')

    def __unicode__(self):
        return self.posicao

    def ocupa_vaga(self):
        self.status = 0

        self.save()

    def desocupa_vaga(self):
        self.status = 1

        self.save()

class Cativa(models.Model):
    id_cativo = models.AutoField(primary_key=True)
    pessoa_id = models.ForeignKey(Pessoa, null=False, blank=False, related_name='pessoa_cativa')
    vaga_id = models.ForeignKey(Vaga, null=False)