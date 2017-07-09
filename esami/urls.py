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

]