from django.db import models
from smgre.estabelecimento.models import Estabelecimento
from smgre.vaga.models import Vaga

# Create your models here.

class Grafo(models.Model):
	id_grafo = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=100, null=True, blank= True)
	estabelecimento = models.ForeignKey(Estabelecimento, null=False, blank=False, related_name='lista_nos')

	def __unicode__(self):
		return self.nome

# G = {'s':{'u':10, 'x':5}, 'u':{'v':1, 'x':2}, 'v':{'y':4}, 'x':{'u':3, 'v':9, 'y':2}, 'y':{'s':7, 'v':6}}

	def monta_grafo(self):
		grafo_dict = {}
		nos_do_grafo = No.objects.filter(grafo=self.id_grafo)

		for no in nos_do_grafo:
			grafo_dict[no.id_no] = {}
			for origem in no.origem_em.all():

				grafo_dict[no.id_no].update({origem.no_destino.id_no: origem.distancia})

		return grafo_dict



class No(models.Model):
    
	id_no = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=100, null=True, blank= True)
	grafo = models.ForeignKey(Grafo, null=False, blank=False, related_name='lista_nos')
	vaga = models.ForeignKey(Vaga, null=True, blank=True, related_name='no_do_grafo')

	longitude = models.IntegerField()
	latitude = models.IntegerField()

	def __unicode__(self):
		return self.nome

class LigaNos(models.Model):
	id_ligacao = models.AutoField(primary_key=True)
	no_origem = models.ForeignKey(No, null=False, blank=False, related_name='origem_em')
	no_destino = models.ForeignKey(No, null=False, blank=False, related_name='destino_em')
	distancia = models.IntegerField()

	def __unicode__(self):
		return "%s => %s" % (self.no_origem.nome, self.no_destino.nome)