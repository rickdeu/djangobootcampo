from django.db import models

class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=100, verbose_name="Nome categoria")
    def __str__(self):
        return self.nome_categoria
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['nome_categoria']

class Perdidos(models.Model):

    class Meta:
        verbose_name = 'Perdido'
        verbose_name_plural = 'Perdidos'
        ordering = ['id','nomecompleto', 'data_perdido']

    nomecompleto = models.CharField(max_length=45, verbose_name="Nome completo")
    tipo_item = models.ForeignKey(Categoria, on_delete = models.CASCADE, related_name = "tipo_perdido", verbose_name ="Categoria")
    numero = models.CharField(max_length=30, verbose_name ="Numero")
    bairro = models.CharField(max_length=30, verbose_name ="Bairro")
    declarante = models.CharField(max_length=30, verbose_name ="Declarante")
    data_perdido = models.DateTimeField(verbose_name="Data")
    date_registo = models.DateTimeField(auto_now_add=True)
    photo1 = models.ImageField(upload_to = "itens_perdidos")
    descricao = models.TextField(max_length = 250, verbose_name = "Descricao")
    resolvido = models.BooleanField(default = False, verbose_name = "Marcar como resolvido")

    def __str__(self):
        return self.nomecompleto


class Achados(models.Model):

    class Meta:
        verbose_name = 'Achado'
        verbose_name_plural = 'Achados'
        ordering = ['id','nomecompleto', 'data_achado']
    nomecompleto = models.CharField(max_length=45, verbose_name="Nome completo")
    tipo_item = models.ForeignKey(Categoria, on_delete = models.CASCADE, related_name = "tipo_achados", verbose_name ="Categoria")
    numero = models.CharField(max_length=30, verbose_name ="Numero")
    bairro = models.CharField(max_length=30, verbose_name ="Bairro")
    declarante = models.CharField(max_length=30, verbose_name ="Declarante")
    data_achado = models.DateTimeField(verbose_name="Data")
    date_registo = models.DateTimeField(auto_now_add=True)
    photo1 = models.ImageField(upload_to = "itens_perdidos")
    descricao = models.TextField(max_length = 250, verbose_name = "Descricao")
    resolvido = models.BooleanField(default = False, verbose_name = "Marcar como resolvido")

    def __str__(self):
        return self.nomecompleto
