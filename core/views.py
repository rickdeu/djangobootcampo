from django.shortcuts import render
from core.models import *

def index(request):
    categoria = Categoria.objects.all()

    perdidos = Perdidos.objects.order_by('-id')[:8]
    ultimo_perdido = Perdidos.objects.order_by('-id')[:1]

    achados = Achados.objects.order_by('-id')[:8]
    ultimo_achados = Achados.objects.order_by('-id')[:1]

    context = {'categoria': categoria, 'perdidos':perdidos, 'ultimo_perdido':ultimo_perdido, 'achados':achados, 'ultimo_achados':ultimo_achados}
    template_name = 'core/index.html'
    return render(request, template_name, context)


def perdidos_lista(request):
    lista_perdidos = Perdidos.objects.all()
    ultimo_perdido = Perdidos.objects.order_by('-id')[:1]
    ultimo_achados = Achados.objects.order_by('-id')[:1]



    template_name = 'core/perdidos.html'

    context = {'lista_perdidos': lista_perdidos, 'ultimo_achados':ultimo_achados, 'ultimo_perdido':ultimo_perdido}
    return render(request, template_name, context)


def achados_lista(request):
    lista_achados = Achados.objects.all()
    ultimo_perdido = Perdidos.objects.order_by('-id')[:1]
    ultimo_achados = Achados.objects.order_by('-id')[:1]



    template_name = 'core/achados.html'

    context = {'lista_achados': lista_achados, 'ultimo_achados':ultimo_achados, 'ultimo_perdido':ultimo_perdido}
    return render(request, template_name, context)