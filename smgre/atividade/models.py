from django.db import models
from smgre.pessoa.models import Pessoa
from smgre.vaga.models import Vaga

# Create your models here.
class Atividade(models.Model):
	id_atividade = models.AutoField(primary_key=True)
	pessoa = models.ForeignKey(Pessoa, null=True, blank=True, related_name='atividade_pessoa')
	entrada = models.DateTimeField('entrada', auto_now_add=True)
	saida = models.DateTimeField('saida',null=True, blank=True)
	vaga = models.ForeignKey(Vaga, null=False, blank=False, related_name='atividade_vaga')

	def calcula_preco(self):
		self.saida = datetime.now()

		minutos_usados = self.saida - self.entrada
		tarifa = self.vaga.tipo_vaga.tarifa
		self.save()
		
		if minutos_usados < tarifa.carencia:
			return 0.0
		else: # a conta de divisao por hora deve sempre contar o teto
			return (minutos_usados/60) * tarifa.preco_hora_adicional + tarifa.preco_inicial
