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
        lista_produse = []
        for pr in produse:
            dict_produs = {}
            dict_produs['cod'] = pr.cod_produs
            dict_produs['nume'] = pr.nume
            print(pr.productset_set.all())
            for prs in pr.productset_set.all():
                if 'cantitate' not in dict_produs:
                    dict_produs['cantitate'] = prs.cantitate
                else:
                    dict_produs['cantitate'] = dict_produs['cantitate'] + prs.cantitate
                if 'raft' not in dict_produs:
                    dict_produs['raft'] = [prs.raft.nume]
                else:
                    if prs.raft.nume not in dict_produs['raft']:
                        dict_produs['raft'].append(prs.raft.nume)
            lista_produse.append(dict_produs)
        print(lista_produse)


        context = {'response':lista_produse}
        return JsonResponse(context)


class ProductSearch(View):










