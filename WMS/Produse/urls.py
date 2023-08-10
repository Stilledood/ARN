from django.urls import path

from .views import ListaProducatori, ListaProduse

urlpatterns = [
    path('lista_producatori/', ListaProducatori.as_view(), name='lista_producatori'),
    path('',ListaProduse.as_view(), name='lista_produse'),

]
