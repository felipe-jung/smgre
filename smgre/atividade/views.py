from django.shortcuts import render_to_response
from smgre.gravo.models import No

def mostra_saida(request, id_no):
	no = No.objects.get(id_no=id_no)

	no_saida = No.objects.get(nome='saida', grafo=no.grafo)

	grafo_dict = no.grafo.monta_grafo()

	lista_ids = shortestPath(grafo_dict, no.id_no, no_saida.id_no)
	for id_no in lista_ids:	
		lista_nos.append(No.objects.get(id_no=id_no))

	return render_to_response('cda/mapas.html',{
		'nos': lista_nos,
		})