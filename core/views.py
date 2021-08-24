from django.shortcuts import render, redirect
from core.models import *
from .form import *

def index(request):
    categoria = Categoria.objects.all()

    perdidos = Perdidos.objects.order_by('-id')[:8]
    ultimo_perdido = Perdidos.objects.order_by('-id')[:1]

    achados = Achados.objects.order_by('-id')[:8]
    ultimo_achados = Achados.objects.order_by('-id')[:1]

    form = PerdidoForm()
    if request.method == 'POST':
        form = PerdidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')





    context = {'categoria': categoria, 'perdidos':perdidos, 'ultimo_perdido':ultimo_perdido, 'achados':achados, 'ultimo_achados':ultimo_achados, 'form':form}
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

def detalhe_perdido(request, pk):
    perdido = Perdidos.objects.get(pk = pk)
    template_name = 'core/detalhe_perdido.html'
    context = {
        'perdido':perdido
    }
    return render(request, template_name, context)