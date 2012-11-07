from django.db import models
from smgre.vaga.models import Vaga
from smgre.estabelecimento.models import Estabelecimento

# Create your models here.

class Vantagem(models.Model):
	id_vantagem = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=100)
	estabelecimento = models.ForeignKey(Estabelecimento, null=False, blank=False, related_name='vantagens')

	def __unicode__(self):
		return self.nome

	def pega_melhor_vaga(self):
		vantagem_vagas_ordenadas = self.vantagem_vantagem.all().order_by('-grau_vantagem')
		for vantagem_vaga in vantagem_vagas_ordenadas:
			if vantagem_vaga.vaga.status == 1:
				return vantagem_vaga.vaga

		return []

class GrauVantagem(models.Model):
	id_grau = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=100)
	grau = models.IntegerField()

	def __unicode__(self):
		return self.nome

class VantagemVaga(models.Model):
	id_vantagem_vaga = models.AutoField(primary_key=True)
	vaga = models.ForeignKey(Vaga, null=False, blank=False, related_name='vantagem_vaga')
	vantagem = models.ForeignKey(Vantagem, null=False, blank=False, related_name='vantagem_vantagem')
	grau_vantagem = models.ForeignKey(GrauVantagem, null=False, blank=False, related_name='vantagem_grau')

	def __unicode__(self):
		return "%s - %s" % (self.vaga.posicao, self.vantagem.nome)