from django import forms
from .models import *
from django.forms import ModelForm

class PerdidoForm(ModelForm):
    class Meta:
        model = Perdidos
        fields = '__all__'
        #exclude = ['resolvido','declarante', 'descricao']
    
    nomecompleto = forms.CharField(
        widget=forms.TextInput(
            attrs={'type':'text', 'class':'form-control', 'placeholder':'Nome completo'}
        ),
        label='Nome completo*',
        max_length=50,
        required=True,
        help_text='Obrigatorio'
    )
    tipo_item = forms.ModelChoiceField(
        queryset= Categoria.objects.select_related().order_by('nome_categoria'),
        widget=forms.Select(attrs={'placeholder':'Categoria', 'class':'form-control'}),
        label='Categoria',
        empty_label='Selecione uma categoria',
        required=True
    )

    numero = forms.CharField(
        widget=forms.TextInput(
            attrs={'type':'text', 'class':'form-control', 'placeholder':'Nº Identificação'}
        ),
        label='Nº de Identificação*',
        max_length=50,
        required=True,
        help_text='Obrigatorio'
    )
    bairro = forms.CharField(
        widget=forms.TextInput(
            attrs={'type':'text', 'class':'form-control', 'placeholder':'Endereço'}
        ),
        label='Endereço*',
        max_length=50,
        required=True,
        help_text='Obrigatorio'
    )

    data_perdido = forms.DateField(
        widget=forms.TextInput(
            attrs={'type':'date', 'class':'form-control', 'placeholder':'Data perdido'}
        ),
        label='Data perdido*',
        required=True,
        help_text='Obrigatorio'
    )
    """descricao = forms.Textarea(
        widget=forms.TextInput(
            attrs={'type':'textarea', 'class':'form-control', 'placeholder':'Data perdido'}
        ),
        label='Data perdido*',
        max_length=50,
        required=True,
        help_text='Obrigatorio'
    )"""

    
