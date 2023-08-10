from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.template.loader import render_to_string

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

        url_parameters = request.GET.get('q')
        lista_produse = []
        if url_parameters:
            produse = self.model_class.objects.filter(nume__icontains=url_parameters)
            if not produse:
                produse = self.model_class.objects.filter(cod_produs__icontains=url_parameters)

        else:
            produse = self.model_class.objects.all()
        for pr in produse:
            dict_produs = {}
            dict_produs['cod'] = pr.cod_produs
            dict_produs['nume'] = pr.nume
            for prs in pr.productset_set.all():
                if 'cantitate' not in dict_produs:
                    dict_produs['cantitate'] = prs.cantitate
                else:
                    dict_produs['cantitate'] = dict_produs['cantitate'] + prs.cantitate
                if 'raft' not in dict_produs:
                    dict_produs['raft'] = {prs.raft.nume:prs.cantitate}
                else:
                    if prs.raft.nume not in dict_produs['raft'].keys():
                        dict_produs['raft'][prs.raft.nume] = prs.cantitate
                    else:
                       dict_produs['raft'][prs.raft.nume] = dict_produs['raft'][prs.raft.nume] + prs.cantitate


            lista_produse.append(dict_produs)
        does_req_accepts_json = request.accepts("aplication/json")
        is_ajax_request = request.headers.get("x-requested_with") == "XMLHttpRequest" and does_req_accepts_json
        if is_ajax_request:
            html = render_to_string(template_name='produse_search_result.html',context={'produse':lista_produse})
            data_dict = {"html_from_view":html}
            return JsonResponse(data=data_dict,safe=False)
        return render(request, template_name="home.html", context={"produse":lista_produse})





        context = {'response':lista_produse}
        return JsonResponse(context)













