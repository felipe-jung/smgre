from django.conf import settings
from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'smgre.views.home', name='home'),
    # url(r'^smgre/', include('smgre.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MAPA_MEDIA}),

    url(r'^vagas/artoolkit/$', 'smgre.vaga.views.vagas_artoolkit'),
    url(r'^vagas/mapa/vantagem/(?P<id_vantagem>[\d]*)$', 'smgre.vaga.views.mostra_vaga'),
    url(r'^vagas/mapa/saida/(?P<id_no_vaga>[\d]*)$', 'smgre.vaga.views.mostra_saida'),
    url(r'^vagas/mapa/pagar/(?P<id_vaga>[\d]*)$', 'smgre.vaga.views.mostra_custo'),
    url(r'^vagas/mapa/vaga/$', 'smgre.vaga.views.show_mapa1'),
    url(r'^estabelecimento/busca_vaga/$', 'smgre.estabelecimento.views.busca_vaga'),
    url(r'^vantagens/estacionamento/(?P<id_estabelecimento>[\d]*)$', 'smgre.vantagem.views.lista_vantagens_por_estabelecimento'),
)
