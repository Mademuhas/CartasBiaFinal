from django.shortcuts import render
from django.views import generic
from .models import Objeto, Escolha
import json
from django.http import JsonResponse

# Create your views here.
class PrincipalView(generic.ListView):
    template_name = "principal.html"
    def get_queryset (self):
        toggle = self.request.GET.get('toggle')
        if toggle:
            aux = Objeto.objects.get(pk=toggle)
            valor = aux.cont
            new_valor = valor + 1
            Objeto.objects.filter(pk=toggle).update(cont = new_valor)
        return Objeto.objects.all().distinct()
    

class LandingView(generic.TemplateView):
    template_name = "landing.html"
class Landing2View(generic.TemplateView):
    template_name = "landing2.html"
class Landing3View(generic.TemplateView):
    template_name = "landing3.html"
class Landing4View(generic.TemplateView):
    template_name = "landing4.html"
class Landing5View(generic.TemplateView):
    template_name = "landing5.html"
    
def salvar_escolha(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        numero_escolhido = data.get('escolha')

        if numero_escolhido is not None:
            escolha = Escolha(nome=numero_escolhido)
            escolha.save()
            return JsonResponse({'mensagem': 'Escolha salva com sucesso!'}, status=201)
        else:
            return JsonResponse({'erro': 'Número inválido'}, status=400)
    
    return JsonResponse({'erro': 'Método não permitido'}, status=405)

class EscolhasListView(generic.ListView):
    model = Escolha
    template_name = "escolhas.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        lista = Escolha.objects.all().order_by('data')
        size = len(lista) - 1
        context['obj1'] = f'static/images/images/{lista[size]}'
        context['obj2'] = f'static/images/images/{lista[size-1]}'
        context['obj3'] = f'static/images/images/{lista[size-2]}'
        context['obj4'] = f'static/images/images/{lista[size-3]}'
        context['obj5'] = f'static/images/images/{lista[size-4]}'

        return context