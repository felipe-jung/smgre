from django.shortcuts import render_to_response
from smgre.estabelecimento.models import Estabelecimento

def busca_vaga(request):
	lista_estabelecimentos = Estabelecimento.objects.all()

	return render_to_response('cda/chegada.html',{
		'estabelecimentos': lista_estabelecimentos,
		})