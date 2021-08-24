from django import forms
from .models import *
from django.forms import ModelForm

class PerdidoForm(ModelForm):
    class Meta:
        model = Perdidos
        fields = '__all__'
        #exclude = ['resolvido',]
    
    nomecompleto = forms.CharField(
        widget=forms.TextInput(
            attrs={'type':'text', 'class':'form-control'}
        ),
        label='Nome completo*',
        max_length=50,
        required=True,
        help_text='Obrigatorio'
    )
    tipo_item = forms.ModelChoiceField(
        queryset= Categoria.objects.select_related().order_by('nome_categoria'),
        widget=forms.Select(attrs={'placeholder':'Categoria'}),
        label='Categoria',
        empty_label='Selecione uma categoria',
        required=True
    )
