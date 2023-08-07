from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

from .models import Produs,Producator,ProductSet

class ListaProducatori(View):
    '''Class to construct a view to dislay a list of all manufacturers'''

    model_class = Producator

    def get(self,request):
        producatori = self.model_class.objects.all()

        context = {}
        for producator in producatori:
            producatori_inventar = {}
            producatori_inventar['Numar Produse'] = producator.produs_set.count()
            for produs in producator.produs_set.all():
                if produs.nume not in producatori_inventar:
                    producatori_inventar[produs.nume] = {}
                    producatori_inventar[produs.nume]['product code'] =produs.cod_produs
                    for prs in produs.productset_set.all():
                        if 'cantitate' not in producatori_inventar[produs.nume]:
                            producatori_inventar[produs.nume]['cantitate'] = prs.cantitate
                        else:
                            producatori_inventar[produs.nume]['cantitate'] = producatori_inventar[produs.nume]['cantitate'] + prs.cantitate
            context[producator.nume] = producatori_inventar
        return JsonResponse(context)


class ListaProduse(View):
    '''Class to construct a list view to display all inventory products'''

    model_class = Produs

    def get(self,request):

        produse = self.model_class.objects.all()
        lista_produse = [{'code':x.cod_produs,'nume':x.nume} for x in produse]
        context = {'response':lista_produse}
       ## for produs in produse:
        ##    inventar_produs = {}
           ## cantitate_total = 0
            ##for produs_set in produs.productset_set.all():
                ##cantitate_total += produs_set.cantitate
                ##raft = produs_set.raft.nume
                ##if raft not in inventar_produs:
                    ##inventar_produs[raft] = produs_set.cantitate
                ##else:
                    ##inventar_produs[raft] = inventar_produs[raft] + produs_set.cantitate
            ##context[produs.nume] = inventar_produs
        return JsonResponse(context)








