from django.conf.urls import url
from esami import views

urlpatterns = [
    url(r'home', views.index, name='index'),
    url(r'getInsegnamenti', views.get_insegnamenti, name='get_insegnamenti'),
    url(r'inserisciInsegnamento', views.insert_insegnamento, name='insert_insegnamento'),
    url(r'getFigure', views.get_figure, name='get_figure'),
    url(r'inserisciFigura', views.insert_figura, name='insert_figura'),
    url(r'getDom', views.get_domande, name='get_domande'),
    url(r'getChiuse', views.get_domande_chiuse, name='get_domande_chiuse'),
    url(r'getAperte', views.get_domande_aperte, name='get_domande_aperte'),
    url(r'inserisciChiusa', views.insert_chiusa, name='insert_chiusa'),
    url(r'inserisciAperta', views.insert_aperta, name='insert_aperta'),
    url(r'getCompiti', views.get_compiti, name='get_compiti'),
    url(r'inserisciCompito', views.insert_compito, name='insert_compito'),
    url(r'getStudenti', views.get_studenti, name='get_studenti'),
    url(r'inserisciStudente', views.insert_studente, name='insert_studente'),
    url(r'getEsami', views.get_esami, name='get_esami'),
    url(r'inserisciEsame', views.insert_esame, name='insert_esame'),
    url(r'getProve', views.get_prove, name='get_prove'),
    url(r'inserisciProva', views.insert_prova, name='insert_prova'),

]