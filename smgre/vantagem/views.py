from django.http import HttpResponse
import json
from smgre.estabelecimento.models import Estabelecimento

def lista_vantagens_por_estabelecimento(request, id_estabelecimento):
	estabelecimento = Estabelecimento.objects.get(id_estabelecimento=id_estabelecimento)
	vantagens = estabelecimento.vantagens.all()
	dict_vantagens = []
	for vantagem in vantagens:
		dict_vantagens.append({'nome':vantagem.nome, 'id':vantagem.id_vantagem})

	return HttpResponse(json.dumps(dict_vantagens))