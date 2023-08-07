from django.urls import path

from .views import ListaProducatori, ListaProduse

urlpatterns = [
    path('', ListaProducatori.as_view(), name='lista_producatori'),
    path('produse/',ListaProduse.as_view(), name='lista_produse'),

]