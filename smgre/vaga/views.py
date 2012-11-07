# Create your views here.
from datetime import datetime
import json
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from smgre.vaga.models import Vaga
from smgre.vantagem.models import Vantagem
from smgre.atividade.models import Atividade
from smgre.grafo.models import Grafo, No
from smgre.dijkstra import shortestPath

@csrf_exempt
def vagas_artoolkit(request):
	post_json = json.loads(request.raw_post_data)
	lista_vagas = post_json['vagas']

	for vaga in lista_vagas:
		try:
			vaga_selecionada = Vaga.objects.get(id_vaga=vaga['id'])
			vaga_selecionada.status = vaga['status']
			vaga_selecionada.save()

		except Vaga.DoesNotExist:
			pass

		print "vaga %s\n" % vaga['id']
		print "status %s" % vaga['status']

	return HttpResponse("Boa garoto")

def mostra_vaga(request, id_vantagem):
	lista_nos = []
	vantagem = Vantagem.objects.get(id_vantagem=id_vantagem)
	melhor_vaga = vantagem.pega_melhor_vaga()

	# if melhor_vaga.len == 0:
	# 	return render_to_response()
	no_vaga = No.objects.get(vaga=melhor_vaga)
	atividade = Atividade(vaga=melhor_vaga)

	melhor_vaga.ocupa_vaga()
	atividade.save()

	grafo = no_vaga.grafo

	grafo_dict = grafo.monta_grafo()
	no_entrada = No.objects.get(grafo=grafo, nome='entrada')

	lista_ids = shortestPath(grafo_dict, no_entrada.id_no, no_vaga.id_no)
	for id_no in lista_ids:	
		lista_nos.append(No.objects.get(id_no=id_no))

	lista_vagas_ocupadas = Vaga.objects.filter(status=0)
	lista_nos_ocupados = []
	for vaga_ocupada in lista_vagas_ocupadas:
		lista_nos_ocupados.append(No.objects.get(vaga=vaga_ocupada))

	url = '/vagas/mapa/pagar/%s' % no_vaga.vaga.id_vaga

	return render_to_response('cda/mapas.html',{
		'nos': lista_nos,
		'url_para_pagar': url,
		'lista_ocupadas': lista_nos_ocupados
		})

def mostra_saida(request, id_no_vaga):
	lista_nos = []

	no_vaga = No.objects.get(id_no=id_no_vaga)
	grafo = no_vaga.grafo

	vaga = no_vaga.vaga
	vaga.desocupa_vaga()

	grafo_dict = grafo.monta_grafo()
	no_saida = No.objects.get(grafo=grafo, nome='saida')

	lista_ids = shortestPath(grafo_dict, no_vaga.id_no, no_saida.id_no)
	for id_no in lista_ids:	
		lista_nos.append(No.objects.get(id_no=id_no))

	lista_vagas_ocupadas = vaga.estabelecimento.obtem_vagas_ocupadas()
	lista_nos_ocupados = []
	for vaga_ocupada in lista_vagas_ocupadas:
		lista_nos_ocupados.append(No.objects.get(vaga=vaga_ocupada))

	return render_to_response('cda/mapas.html',{
		'nos': lista_nos,
		'lista_ocupadas': lista_nos_ocupados
		})

def mostra_custo(request, id_vaga):
	atividade = Atividade.objects.get(vaga=id_vaga, saida=None)

	preco = atividade.calcula_preco()

	no_vaga = No.objects.get(vaga=id_vaga)
	url = '/vagas/mapa/saida/%s' % no_vaga.id_no

	return render_to_response('cda/pagamento.html',{
		'preco': preco,
		'url_saida': url
		})

def show_mapa1(request):
	lista_nos = []
	# vaga = Vaga.objects.get(id_vaga=id_vaga)
	# no_vaga = No.objects.get(vaga=vaga)
	# grafo = no_vaga.grafo

	# grafo_dict = grafo.monta_grafo()
	# no_entrada = No.objects.get(grafo=grafo, nome='entrada')

	lista_ids = []#shortestPath(grafo_dict, no_entrada.id_no, no_vaga.id_no)
	for id_no in lista_ids:	
		lista_nos.append(No.objects.get(id_no=id_no))

	return render_to_response('cda/mapas.html',{
		'nos': lista_nos,
		})